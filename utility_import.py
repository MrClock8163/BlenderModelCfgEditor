import bpy
import os
from . import utility as Utils
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
    trim = False
    decimal = False
    trimmedOp = ""
    
    for i in range(len(expression)):
        char = expression[i]
        
        if char == "0" and (expression[i+1] if (i+1 <= len(expression)-1) else "") == ".":
            decimal = True
        
        if char == "0" and not decimal:
            trim = True
            
        if char in "()+-/*^123456789":
            trim = False
            decimal = False
            
        if not trim:
            trimmedOp += char
            
    return trimmedOp

# Evaluate string expression
def StringToFloat(value):
    returnValue = 0
    
    if type(value) is str:
        value = value.strip()
        value = TrimZeros(value)
    
    try:
        eval(value)
    except:
        returnValue = 0
    else:
        returnValue = eval(value)
    
    return returnValue

# Create skeleton class and other related nodes
def ImportSkeletons(CfgSkeletons,createLinks):
    
    nodeTree = bpy.context.space_data.node_tree
    
    allNodes = []
    
    if type(CfgSkeletons) is str:
        return allNodes
    
    # crate nodes
    for className in CfgSkeletons.elements:
        nodes = []
        
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
        
    return allNodes

# Create model class and related nodes
def ImportModels(CfgModels,CfgSkeletons,CfgSkeletonsNodes,createLinks,omitAnims):
    nodeTree = bpy.context.space_data.node_tree
    
    allNodes = []
    
    if type(CfgModels) is str:
        return allNodes
    
    startX = (len(CfgSkeletonsNodes) * 600) + 200
    
    # create nodes
    for className in CfgModels.elements:
        nodes = []
        
        newModel = getattr(CfgModels,className)
        
        newModelNode = nodeTree.nodes.new("MCFG_N_Model")
        newModelNode.modelName = newModel.name
        newModelNode.location = [startX + len(allNodes) * 800,-300]
        
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
            
            if len(modelSections) != 0:
                newSectionListNode = nodeTree.nodes.new("MCFG_N_SectionList")
                newSectionListNode.sectionCount = len(modelSections)
                newSectionListNode.location = [startX + len(allNodes) * 800 - 200,-400]
                
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
                newModelAnimListNode = nodeTree.nodes.new("MCFG_N_AnimationList")
                newModelAnimListNode.animCount = len(modelAnims.elements)
                newModelAnimListNode.location = [startX + len(allNodes) * 800 - 400,-400]
                
                if createLinks != 'NONE':
                    nodeTree.links.new(newModelAnimListNode.outputs[0],newModelNode.inputs[4])
                
                animNodes = []
                
                for i in range(len(modelAnims.elements)):
                    modelAnim = getattr(modelAnims,modelAnims.elements[i])
                    
                    newModelAnimNode = nodeTree.nodes.new("MCFG_N_Animation")
                    newModelAnimNode.location = [startX + len(allNodes) * 800 - 600,-300 - len(animNodes) * 400]
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
                       
                    # handle minValue
                    if hasattr(modelAnim,"minvalue"):
                        value = modelAnim.minvalue
                        
                        if value.lower().startswith("("):
                            value = value[1:-1].strip()
                            
                        if type(value) is str and value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[8].isDeg = True
                        
                        newModelAnimNode.inputs[8].floatValue = StringToFloat(value)
                    else:
                        newModelAnimNode.overrideMinValue = False
                    
                    # handle maxValue
                    if hasattr(modelAnim,"maxvalue"):
                        value = modelAnim.maxvalue
                        
                        if value.lower().startswith("("):
                            value = value[1:-1].strip()
                        
                        if type(value) is str and value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[9].isDeg = True
                        
                        newModelAnimNode.inputs[9].floatValue = StringToFloat(value)
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
                        value = getattr(modelAnim,valueName)
                        
                        if value.lower().startswith("("):
                            value = value[1:-1].strip()
                        
                        if value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[10].isDeg = True
                        
                        newModelAnimNode.inputs[10].floatValue = StringToFloat(value)
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
                        value = getattr(modelAnim,valueName)
                        
                        if value.lower().startswith("("):
                            value = value[1:-1].strip()
                        
                        if value.lower().startswith("rad"):
                            value = value[3:]
                            newModelAnimNode.inputs[11].isDeg = True
                        
                        newModelAnimNode.inputs[11].floatValue = StringToFloat(value)
                    else:
                        newModelAnimNode.overrideTypeMaxValue = False
                
        nodes.append(sectionListNodes)
        
        allNodes.append(nodes)
    
    return allNodes

# Import model.cfg file
def ImportFile(self,context):
    # Read settings
    importOnlySkeletons = context.scene.MCFG_SP_ImportDepth == 'SKELETONS'
    omitAnims = context.scene.MCFG_SP_ImportDepth == 'MODELS'
    createLinks = context.scene.MCFG_SP_ImportLinkDepth
    
    toolsFolder = bpy.context.preferences.addons[__package__].preferences.armaToolsFolder
    
    exePath = os.path.join(toolsFolder,"CfgConvert\CfgConvert.exe")
    
    if not os.path.isfile(exePath):
        Utils.ShowInfoBox("CfgConvert.exe does not exists","Error",'ERROR')
        return
    
    # Convert and get config in class structure
    classTree = XML.ReadConfig(self.filepath,exePath)
    
    # Create new node tree
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
    skeletonNodes = []
    modelNodes = []
    
    if "cfgskeletons" in classTree.elements:
        skeletonNodes = ImportSkeletons(classTree.cfgskeletons,createLinks)
    
    if not importOnlySkeletons and "cfgmodels" in classTree.elements:
        modelNodes = ImportModels(classTree.cfgmodels,classTree.cfgskeletons,skeletonNodes,createLinks,omitAnims)
        
