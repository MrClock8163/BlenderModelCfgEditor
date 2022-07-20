import bpy
import os
import re
from . import utility as Utils
from .utility_print import LogFormatter as Logger
from . import utility_import_xml as XML

# Parse string and int values to boolean
def ParseBool(value):
    
    if type(value) is str and (value.lower() == "false" or value.lower() == "0"):
        return False
    
    if type(value) is int and value == 0:
        return False
    
    return True

# Trim leading zeros from numbers in simple string expression
def TrimZeros(expression):

    numbers = (re.sub("\+|\-|\*|/|^|\(|\)"," ",expression)).split() # filter out operators and get numbers
    numbers = [num.strip().lstrip("0") for num in numbers] # strip "0"-s from left side
        
    operations = re.sub("[0-9]|[.]","_",expression) # filter out numbers and replace with underscores
    operations = re.split("[_]+",operations) # split at underscores
    operations = "{}".join(operations) # join to formatter format
    
    result = operations.format(*numbers) # join operators with numbers
    
    if result == "": # failsafe for when the input was "0" and ended up stripped entirely
        result = "0"
    
    return result

# Evaluate string expression
def StringToFloat(value):
    returnValue = 0
    
    if type(value) is str:
        value = value.strip()
        value = TrimZeros(value)
    
    try:
        eval(value)
    except:
        print(Logger.Log("Could not evaluate expression: '{}'".format(value),6))
        print(Logger.Log("Default value 0",6))
        returnValue = 0
    else:
        returnValue = eval(value)
    
    return returnValue

# Create skeleton class and other related nodes
def ImportSkeletons(CfgSkeletons,createLinks):
    
    print(Logger.Log("Started CfgSkeletons",2))
    
    nodeTree = bpy.context.space_data.node_tree
    
    allNodes = []
    
    if type(CfgSkeletons) is str:
        print(Logger.Log("Finished CfgSkeletons",2))
        return allNodes
    
    # crate nodes
    for className in CfgSkeletons.elements:
        nodes = []
        
        print(Logger.Log("Creating skeleton node: {}".format(className),3))
        
        newSkeleton = getattr(CfgSkeletons,className)
        
        newSkeletonNode = nodeTree.nodes.new("MCFG_N_Skeleton")
        newSkeletonNode.skeletonName = newSkeleton.name
        newSkeletonNode.location = [0 + len(allNodes) * 600, 0]
        
        # create parenting links
        if newSkeleton.parent != "" and createLinks != 'NONE':
            skeletonParentIndex = CfgSkeletons.elements.index(newSkeleton.parent)
            nodeTree.links.new(allNodes[skeletonParentIndex][0].outputs[0],newSkeletonNode.inputs[0])
        
        # handle skeletonInherit
        if hasattr(newSkeleton,"skeletoninherit"):
            skeletonInherit = getattr(newSkeleton,"skeletoninherit")
            if skeletonInherit != "" and createLinks != 'NONE':
                skeletonInheritIndex = CfgSkeletons.elements.index(skeletonInherit)
                nodeTree.links.new(allNodes[skeletonInheritIndex][0].outputs[0],newSkeletonNode.inputs[1])
        else:
            newSkeletonNode.overrideInheritBones = False
            
        # handle isDiscrete
        if hasattr(newSkeleton,"isdiscrete"):
            skeletonIsDiscrete = getattr(newSkeleton,"isdiscrete")
            newSkeletonNode.inputs[2].boolValue = ParseBool(skeletonIsDiscrete)
        else:
            newSkeletonNode.overrideIsDiscrete = False
        
        nodes.append(newSkeletonNode)
        
        boneListNodes = []
        boneNodes = []
        
        # handle skeletonBones
        if hasattr(newSkeleton,"skeletonbones"):
            if len(getattr(newSkeleton,"skeletonbones")) != 0:
                print(Logger.Log("Creating bone list",4))
                newBoneListNode = nodeTree.nodes.new("MCFG_N_BoneList")
                boneList = getattr(newSkeleton,"skeletonbones")
                newBoneListNode.location = [-200 + len(allNodes) * 600, -100]
                
                if createLinks != 'NONE':
                    nodeTree.links.new(newBoneListNode.outputs[0],newSkeletonNode.inputs[3])
                
                boneListNodes.append(newBoneListNode)
                
                # separate bones and their parents from the list
                bones = []
                boneParents = []
                for i in range(len(boneList)):
                    if i % 2 == 0:
                        bones.append(boneList[i])
                    else:
                        boneParents.append(boneList[i])
                
                newBoneListNode.boneCount = len(bones)
                
                # create bone nodes
                for i in range(len(bones)):
                    bone = bones[i]
                    
                    print(Logger.Log("Creating bone node: {}".format(bone),5))
                    
                    newBoneNode = nodeTree.nodes.new("MCFG_N_Bone")
                    newBoneNode.boneName = bone
                    newBoneNode.location = [-400 + len(allNodes) * 600, 0 - len(boneNodes) * 100]
                    
                    if createLinks == 'ALL':
                        nodeTree.links.new(newBoneNode.outputs[0],newBoneListNode.inputs[len(boneNodes)])
                    
                    if boneParents[i] != "" and createLinks != 'NONE':
                        boneParentIndex = bones.index(boneParents[i])
                        nodeTree.links.new(boneNodes[boneParentIndex].outputs[0],newBoneNode.inputs[0])
                    
                    boneNodes.append(newBoneNode)
        else:
            newSkeletonNode.overrideBones = False
                
        nodes.append(boneListNodes)
        nodes.append(boneNodes)
        allNodes.append(nodes)
        
    print(Logger.Log("Finished CfgSkeletons",2))
        
    return allNodes

# Create model class and related nodes
def ImportModels(CfgModels,CfgSkeletons,CfgSkeletonsNodes,createLinks,omitAnims,handleExpressions):

    print(Logger.Log("Started CfgModels",2))
    
    nodeTree = bpy.context.space_data.node_tree
    
    allNodes = []
    
    if type(CfgModels) is str:
        return allNodes
    
    startX = (len(CfgSkeletonsNodes) * 600) + 200
    
    # create nodes
    for className in CfgModels.elements:
        nodes = []
        
        print(Logger.Log("Creating model node: {}".format(className),3))
        
        newModel = getattr(CfgModels,className)
        
        newModelNode = nodeTree.nodes.new("MCFG_N_Model")
        newModelNode.modelName = newModel.name
        newModelNode.location = [startX + len(allNodes) * 1000,-300]
        
        # create parenting links
        if newModel.parent != "" and createLinks != 'NONE':
            modelParentIndex = CfgModels.elements.index(newModel.parent)
            nodeTree.links.new(allNodes[modelParentIndex][0].outputs[0],newModelNode.inputs[0])
        
        nodes.append(newModelNode)
        
        # handle sectionsInherit
        if hasattr(newModel,"sectionsinherit"):
            sectionsInherit = getattr(newModel,"sectionsinherit")
            if sectionsInherit != "" and createLinks != 'NONE':
                sectionsInheritIndex = CfgModels.elements.index(sectionsInherit)
                nodeTree.links.new(allNodes[sectionsInheritIndex][0].outputs[0],newModelNode.inputs[1])
        else:
            newModelNode.overrideInheritSections = False
        
        # handle skeletonName
        if hasattr(newModel,"skeletonname"):
            modelSkeletonName = getattr(newModel,"skeletonname")
            if modelSkeletonName != "" and createLinks != 'NONE':
                modelSkeletonIndex = CfgSkeletons.elements.index(modelSkeletonName)
                nodeTree.links.new(CfgSkeletonsNodes[modelSkeletonIndex][0].outputs[0],newModelNode.inputs[2])
            
        else:
            newModelNode.overrideSkeleton = False
        
        # handle sections
        sectionListNodes = []
        
        if hasattr(newModel,"sections"):
            modelSections = getattr(newModel,"sections")
            
            print(Logger.Log("Creating sections",4))
        
            if len(modelSections) != 0:
                newSectionListNode = nodeTree.nodes.new("MCFG_N_SectionList")
                newSectionListNode.sectionCount = len(modelSections)
                newSectionListNode.location = [startX + len(allNodes) * 1000 - 200,-400]
                
                if createLinks != 'NONE':
                    nodeTree.links.new(newSectionListNode.outputs[0],newModelNode.inputs[3])
                
                sectionListNodes.append(newSectionListNode)
                
                for i in range(len(modelSections)):
                    newSectionListNode.inputs[i].stringValue = modelSections[i]
            
        else:
            newModelNode.overrideSections = False

        # handle animations
        if hasattr(newModel,"animations") and getattr(newModel,"animations") != "" and not omitAnims: # potential problem
            modelAnims = getattr(newModel,"animations")
            
            if modelAnims.parent != "":
                newModelNode.overrideAnimations = True
            
            if len(modelAnims.elements) != 0:
                print(Logger.Log("Creating animation list",4))
                newModelAnimListNode = nodeTree.nodes.new("MCFG_N_AnimationList")
                newModelAnimListNode.animCount = len(modelAnims.elements)
                newModelAnimListNode.location = [startX + len(allNodes) * 1000 - 400,-400]
                
                if createLinks != 'NONE':
                    nodeTree.links.new(newModelAnimListNode.outputs[0],newModelNode.inputs[4])
                
                animNodes = []
                
                for i in range(len(modelAnims.elements)):
                    modelAnim = getattr(modelAnims,modelAnims.elements[i])
                    print(Logger.Log("Creating animation node: {}".format(modelAnim.name),5))
                    
                    newModelAnimNode = nodeTree.nodes.new("MCFG_N_Animation")
                    newModelAnimNode.location = [startX + len(allNodes) * 1000 - 600,-300 - len(animNodes) * 400]
                    newModelAnimNode.animName = modelAnim.name
                    
                    # create parenting links
                    if modelAnim.parent != "" and createLinks != 'NONE':
                        animParentIndex = modelAnims.elements.index(modelAnim.parent)
                        nodeTree.links.new(animNodes[animParentIndex].outputs[0],newModelAnimNode.inputs[0])
                    
                    if createLinks == 'ALL':
                        nodeTree.links.new(newModelAnimNode.outputs[0],newModelAnimListNode.inputs[i])
                        
                    animNodes.append(newModelAnimNode)
                    
                    # handle animation type
                    if hasattr(modelAnim,"type"):
                        animType = modelAnim.type.upper()
                    else:
                        animType = 'TRANSLATION'
                        parent = modelAnim.parent
                        
                        while parent != "":
                            parentClass = getattr(modelAnims,parent)
                            if hasattr(parentClass,"type"):
                                animType = getattr(parentClass,"type").upper()
                                break
                            parent = parentClass.parent
                    
                    newModelAnimNode.animType = animType
                    
                    # handle source
                    if hasattr(modelAnim,"source"):
                        if modelAnim.source == "":
                            newModelAnimNode.inputs[1].stringValue = "empty"
                        else:
                            newModelAnimNode.inputs[1].stringValue = modelAnim.source
                    else:
                        newModelAnimNode.overrideSource = False
                            
                    # handle sourceAddress
                    if hasattr(modelAnim,"sourceaddress"):
                        newModelAnimNode.inputs[2].typeValue = modelAnim.sourceaddress.upper()
                    else:
                        newModelAnimNode.overrideSourceAddress = False
                    
                    # handle selection
                    if hasattr(modelAnim,"selection"):
                        if modelAnim.selection == "":
                            newModelAnimNode.inputs[3].stringValue = "empty"
                        else:
                            newModelAnimNode.inputs[3].stringValue = modelAnim.selection
                    else:
                        newModelAnimNode.overrideSelection = False
                    
                    # handle axis related inputs
                    if animType != 'HIDE':
                        # handle memory
                        if hasattr(modelAnim,"memory"):
                            newModelAnimNode.inputs[4].boolValue = ParseBool(modelAnim.memory)
                        else:
                            newModelAnimNode.overrideMemory = False
                        
                        # handle axis
                        if hasattr(modelAnim,"axis"):
                            newModelAnimNode.axisType = 'AXIS'
                            newModelAnimNode.inputs[5].stringValue = modelAnim.axis
                            
                        elif hasattr(modelAnim,"begin") or hasattr(modelAnim,"end"):
                            newModelAnimNode.axisType = 'POINTS'
                            
                            # handle begin
                            if hasattr(modelAnim,"begin"):
                                newModelAnimNode.inputs[6].stringValue = modelAnim.begin
                            else:
                                newModelAnimNode.overrideBegin = False
                            
                            # handle end
                            if hasattr(modelAnim,"end"):
                                newModelAnimNode.inputs[7].stringValue = modelAnim.end
                            else:
                                newModelAnimNode.overrideEnd = False
                        
                        else:
                            newModelAnimNode.axisType = 'AXIS'
                            newModelAnimNode.overrideAxis = False
                        
                    else:
                        newModelAnimNode.inputs[4].enabled = False
                        newModelAnimNode.inputs[5].enabled = False
                    
                    expressionNodes = 0
                    
                    # handle minValue
                    if hasattr(modelAnim,"minvalue"):
                        value = modelAnim.minvalue.strip()
                        
                        if value.lower()[0] == "(" and value.lower()[-1] == ")":
                            value = value[1:-1].strip()
                            
                        if type(value) is str and value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[8].isDeg = True
                        
                        if handleExpressions == 'EVAL':
                            newModelAnimNode.inputs[8].floatValue = StringToFloat(value)
                            
                        else:
                            try:
                                float(value)
                                
                                if handleExpressions == 'PRESERVE': # force exception to run node creation code
                                    raise Exception
                                    
                            except:
                                expressionNode = nodeTree.nodes.new("MCFG_N_MathExpression")
                                expressionNode.expression = value
                                expressionNode.isDeg = newModelAnimNode.inputs[8].isDeg
                                expressionNode.location = [startX + len(allNodes) * 1000 - 800,-300 - (len(animNodes) - 1) * 400 - expressionNodes * 80]
                                
                                if createLinks != 'NONE':
                                    nodeTree.links.new(expressionNode.outputs[0],newModelAnimNode.inputs[8])
                                
                                expressionNodes += 1
                            else:
                                newModelAnimNode.inputs[8].floatValue = float(value)
                        
                    else:
                        newModelAnimNode.overrideMinValue = False
                    
                    # handle maxValue
                    if hasattr(modelAnim,"maxvalue"):
                        value = modelAnim.maxvalue.strip()
                        
                        if value.lower()[0] == "(" and value.lower()[-1] == ")":
                            value = value[1:-1].strip()
                        
                        if type(value) is str and value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[9].isDeg = True
                        
                        if handleExpressions == 'EVAL':
                            newModelAnimNode.inputs[9].floatValue = StringToFloat(value)
                            
                        else:
                            try:
                                float(value)
                                
                                if handleExpressions == 'PRESERVE': # force exception to run node creation code
                                    raise Exception
                                    
                            except:
                                expressionNode = nodeTree.nodes.new("MCFG_N_MathExpression")
                                expressionNode.expression = value
                                expressionNode.isDeg = newModelAnimNode.inputs[9].isDeg
                                expressionNode.location = [startX + len(allNodes) * 1000 - 800,-300 - (len(animNodes) - 1) * 400 - expressionNodes * 80]
                                
                                if createLinks != 'NONE':
                                    nodeTree.links.new(expressionNode.outputs[0],newModelAnimNode.inputs[9])
                                
                                expressionNodes += 1
                            else:
                                newModelAnimNode.inputs[9].floatValue = float(value)
                    else:
                        newModelAnimNode.overrideMaxValue = False
                    
                    # handle type specific min value
                    valueName = ""
                    if hasattr(modelAnim,"offset0"):
                        valueName = "offset0"
                    elif hasattr(modelAnim,"angle0"):
                        valueName = "angle0"
                    elif hasattr(modelAnim,"hidevalue"):
                        valueName = "hidevalue"
                    
                    if valueName != "":
                        value = getattr(modelAnim,valueName).strip()
                        
                        if value.lower()[0] == "(" and value.lower()[-1] == ")":
                            value = value[1:-1].strip()
                        
                        if value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[10].isDeg = True
                        
                        if handleExpressions == 'EVAL':
                            newModelAnimNode.inputs[10].floatValue = StringToFloat(value)
                            
                        else:
                            try:
                                float(value)
                                
                                if handleExpressions == 'PRESERVE': # force exception to run node creation code
                                    raise Exception
                                    
                            except:
                                expressionNode = nodeTree.nodes.new("MCFG_N_MathExpression")
                                expressionNode.expression = value
                                expressionNode.isDeg = newModelAnimNode.inputs[10].isDeg
                                expressionNode.location = [startX + len(allNodes) * 1000 - 800,-300 - (len(animNodes) - 1) * 400 - expressionNodes * 80]
                                
                                if createLinks != 'NONE':
                                    nodeTree.links.new(expressionNode.outputs[0],newModelAnimNode.inputs[10])
                                
                                expressionNodes += 1
                            else:
                                newModelAnimNode.inputs[10].floatValue = float(value)
                    else:
                        newModelAnimNode.overrideTypeMinValue = False
                        
                    # handle type specific max value
                    valueName = ""
                    if hasattr(modelAnim,"offset1"):
                        valueName = "offset1"
                    elif hasattr(modelAnim,"angle1"):
                        valueName = "angle1"
                    elif hasattr(modelAnim,"unhidevalue"):
                        valueName = "unhidevalue"
                    
                    if valueName != "":
                        value = getattr(modelAnim,valueName).strip()
                        
                        if value.lower()[0] == "(" and value.lower()[-1] == ")":
                            value = value[1:-1].strip()
                        
                        if value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[11].isDeg = True
                        
                        if handleExpressions == 'EVAL':
                            newModelAnimNode.inputs[8].floatValue = StringToFloat(value)
                            
                        else:
                            try:
                                float(value)
                                
                                if handleExpressions == 'PRESERVE': # force exception to run node creation code
                                    raise Exception
                                    
                            except:
                                expressionNode = nodeTree.nodes.new("MCFG_N_MathExpression")
                                expressionNode.expression = value
                                expressionNode.isDeg = newModelAnimNode.inputs[11].isDeg
                                expressionNode.location = [startX + len(allNodes) * 1000 - 800,-300 - (len(animNodes) - 1) * 400 - expressionNodes * 80]
                                
                                if createLinks != 'NONE':
                                    nodeTree.links.new(expressionNode.outputs[0],newModelAnimNode.inputs[1])
                                
                                expressionNodes += 1
                            else:
                                newModelAnimNode.inputs[11].floatValue = float(value)
                    else:
                        if animType == 'HIDE': # failsafe for when unhideValue is omitted from the config entirely
                            newModelAnimNode.inputs[11].floatValue = -1
                            
                        newModelAnimNode.overrideTypeMaxValue = False
                
        nodes.append(sectionListNodes)
        
        allNodes.append(nodes)
        
    print(Logger.Log("Finished CfgModels",2))
    
    return allNodes

# Import model.cfg file
def ImportFile(self,context):
    
    print(Logger.LogTitle("Started mcfg import"))

    # Read settings
    print(Logger.Log("Read settings",1))
    
    importOnlySkeletons = context.scene.MCFG_SP_ImportDepth == 'SKELETONS'
    omitAnims = context.scene.MCFG_SP_ImportDepth == 'MODELS'
    createLinks = context.scene.MCFG_SP_ImportLinkDepth
    handleExpressions = context.scene.MCFG_SP_ImportExpressions
    
    toolsFolder = bpy.context.preferences.addons[__package__].preferences.armaToolsFolder
    
    exePath = os.path.join(toolsFolder,"CfgConvert\CfgConvert.exe")
    
    if not os.path.isfile(exePath):
        Utils.ShowInfoBox("CfgConvert.exe does not exist","Error",'ERROR')
        print(Logger.Log("CfgConvert.exe does not exist in the specified directory",1))
        return
    
    # Convert and get config in class structure
    print(Logger.Log("Started model.cfg reading",1))
    classTree = XML.ReadConfig(self.filepath,exePath)
    print(Logger.Log("Finished model.cfg reading",1))
    
    # Create new node tree
    print(Logger.Log("Created new node tree",1))
    space = context.space_data
    newtree = bpy.data.node_groups.new("Imported", "MCFG_N_Tree")
    newtree.use_fake_user = True
    space.node_tree = newtree
    
    # Create commented frame node with import path note
    commentTextData = "Imported model configuration\nSource path: {}".format(self.filepath)
    commentText = bpy.data.texts.new("Import comment")
    commentText.write(commentTextData)
    
    frameComment = newtree.nodes.new("NodeFrame")
    frameComment.location = [0,200]
    frameComment.label = "Comment"
    frameComment.shrink = False
    frameComment.height = 120
    frameComment.width = len(commentTextData.split("\n")[1]) * 15
    frameComment.text = commentText
    
    # Create nodes
    print(Logger.Log("Started creating nodes",1))
    
    skeletonNodes = []
    modelNodes = []
    
    if "cfgskeletons" in classTree.elements:
        skeletonNodes = ImportSkeletons(classTree.cfgskeletons,createLinks)
    
    if not importOnlySkeletons and "cfgmodels" in classTree.elements:
        modelNodes = ImportModels(classTree.cfgmodels,classTree.cfgskeletons,skeletonNodes,createLinks,omitAnims,handleExpressions)
        
    print(Logger.Log("Finished creating nodes",1))
    print(Logger.LogTitle("Finished mcfg import"))