import bpy
import os
import webbrowser

from .utility_print import ConfigFormatter
from . import utility_data as Data

# Info pop-up that appears at the cursor position
def ShowInfoBox(message,title = "",icon = 'INFO'):
    def draw(self,context):
        self.layout.label(text = message)
    bpy.context.window_manager.popup_menu(draw,title = title,icon = icon)

# Run the .process() function on all connected nodes consequently
def ProcessNodeTree(context):
    
    CfgSkelly = Data.CfgSkeletons()
    CfgMesh = Data.CfgModels()
    
    nodeTree = context.space_data.node_tree
    
    for node in nodeTree.nodes:
        if node.process_type == "skeleton" and node.exportClass:
            newSkeleton = node.process()
            
            CfgSkelly.AddSkeleton(newSkeleton)
        
        if node.process_type == "model" and node.exportClass:
            newModel = node.process()
            CfgMesh.AddModel(newModel)

    return [CfgSkelly,CfgMesh]

# Validate the data class structure produced by the ProcessNodeTree function
def ValidateClassStructure(CfgSkeletons,CfgModels):

    addonPrefs = bpy.context.preferences.addons[__package__].preferences
    warnsAreErrs = addonPrefs.warnsAreErr
    logFile = None
    
    if addonPrefs.validationOutput == 'FILE':
        logFile = open(bpy.context.scene.modelCfgExportDir + "model.cfg.log","w")

    isValid = True
    
    validator = Data.ValidationInfo()
    
    validator = CfgSkeletons.Validate(validator)
    validator = CfgModels.Validate(validator)
    
    print("==========================================" + ConfigFormatter.Endl(),file=logFile)
    
    print(validator.Print(),file=logFile)
    isValid = validator.Evaluate(warnsAreErrs)
    
    verdict = ""
    if isValid:
        verdict = "The data structure is valid"
    else:
        verdict = "The data structure is not valid"
        
    print(verdict + ConfigFormatter.Endl(),file=logFile)
    
    print("==========================================",file=logFile)
    
    if logFile is not None:
        logFile.close()

    return [isValid,[validator.CountErr(),validator.CountWarn()]]

# Process, validate and (if necessary) export
def ExportFile(self,context,export = True):

    nodeTree = context.space_data.node_tree
    
    # Preliminary checks
    if len(nodeTree.nodes) == 0:
        ShowInfoBox("There are no nodes in the tree",title = "Info",icon = 'INFO')
        return
        
    for link in nodeTree.links:
        if not link.is_valid:
            ShowInfoBox("There are invalid links in the tree",title = "Error",icon = 'ERROR')
            return
    
    # Process setup
    [CfgSkelly,CfgMesh] = ProcessNodeTree(context)
    couldSortSkelly = CfgSkelly.SortParenting()
    couldSortMesh = CfgMesh.SortParenting()
    
    # Second preliminary checks
    if not CfgSkelly.Unique() or not CfgMesh.Unique():
        ShowInfoBox("The class names are not unique",title = "Error",icon = 'ERROR')
        return
    
    if not couldSortSkelly or not couldSortMesh:
        ShowInfoBox("Couldn't sort parenting",title = "Error",icon = 'ERROR')
        return
    
    # Validation
    [isValidData,counts] = ValidateClassStructure(CfgSkelly,CfgMesh)
    if not isValidData and not context.scene.modelCfgEditorIgnoreErrors:
        verdict = ["Validation failed","Export failed"]
    else:
        verdict = ["Validation successful","Export successful"]
        
    reportlines = ["Number of warnings: " + str(counts[1]),"Number of errors: " + str(counts[0]),"See the log for more info"]
    reportFinal = ",".join(reportlines)
    
    if export:
        reportFinal += ("|" + verdict[1].upper())
    else:
        reportFinal += ("|" + verdict[0].upper())
    
    bpy.ops.mcfg.reportbox('INVOKE_DEFAULT',report=reportFinal)
    
    if (not isValidData and not context.scene.modelCfgEditorIgnoreErrors) or not export:
        return
    
    # Export
    if not os.path.exists(context.scene.modelCfgExportDir) and export:
        ShowInfoBox("No valid file location was specified","Error",'ERROR')
        self.report({'ERROR'},"No valid output location was given for model.cfg export")
        return
        
    exportFile = open(context.scene.modelCfgExportDir + "model.cfg","w")
    
    print(CfgSkelly.Print(),file=exportFile)
    print(CfgMesh.Print(),file=exportFile)
    
    exportFile.close()
    
    if context.scene.modelCfgEditorOpenNotepad:
        webbrowser.open(context.scene.modelCfgExportDir + "model.cfg")
    
# Print inspected data
def InspectData(self,context):
    nodeTree = context.space_data.node_tree
    
    inspectors = 0
    for node in nodeTree.nodes:
        if node.process_type == "inspector" and node.active:
            inspectors += 1
            node.inspect()
            
    if inspectors == 0:
        ShowInfoBox("There are no active inspector nodes","Info",'INFO')
    else:
        ShowInfoBox("Check System Log for inspection output","Info",'INFO')

# Create bone nodes from the selected selections of the active model
def CreateBoneNodes(self,context):
    nodeTree = context.space_data.node_tree
    selections = bpy.context.scene.ModelSelectionList
    
    boneCount = 0
    nodeList = []
    
    for i in range(len(selections)):
        selection = selections[i]
        if selection.include:
            newNode = nodeTree.nodes.new("MCFG_N_Bone")
            newNode.boneName = selection.name
            newNode.location = [0,boneCount * -100]
            nodeList.append(newNode)
            boneCount += 1
    
    # create list node if desired
    if context.scene.ModelSelectionListListNode and len(nodeList) > 0:
        listNode = nodeTree.nodes.new("MCFG_N_BoneList")
        listNode.location = [200,0]
        listNode.boneCount = len(nodeList)
        
        for i in range(len(nodeList)):
            nodeTree.links.new(nodeList[i].outputs[0],listNode.inputs[i])
        
        context.scene.ModelSelectionListListNode = False

# Create section list node from the selected selections of the active model
def CreateSectionNodes(self,context):
    nodeTree = context.space_data.node_tree
    selections = bpy.context.scene.ModelSelectionList
    
    newSections = []
    for i in range(len(selections)):
        selection = selections[i]
        
        if selection.include:
            newSections.append(selection.name)
    
    newNode = nodeTree.nodes.new("MCFG_N_SectionList")
    newNode.location = [0,0]
    newNode.sectionCount = len(newSections)
    
    for i in range(len(newSections)):
        newNode.inputs[i].stringValue = newSections[i]