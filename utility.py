import bpy
import os

from .utility_print import InfoFormatter, ConfigFormatter
from . import utility_data as Data

class InfoTypes:
    @classmethod
    def ErrNone(cls):
        return "no errors were found"

    @classmethod
    def ErrClassName(cls,name):
        return ("invalid class name: " + InfoFormatter.Quote(name))

class InfoItem:
    type = "e"
    info = ""
    
    def __init__(self,infoText,infoType = "e"):
        if not infoType in ["e","w","i"]:
            infoType = "e"
        
        self.info = infoText
        self.type = infoType

class TreeInfo:
    infoList = []
    errCount = 0
    warnCount = 0
    infoCount = 0
    
    def __init__(self):
        self.infoList = []
        self.errCount = 0
        self.warnCount = 0
        self.infoCount = 0
        
    def AddInfo(self,newItem):
        if newItem.type == "e":
            self.errCount += 1
        elif newItem.type == "w":
            self.warnCount += 1
        elif newItem.type == "i":
            self.infoCount += 1
            
        self.infoList.append(newItem)
        
    def Print(self,writeAll = False, logFile = None):
        
        if len(self.infoList) == 0 and not writeAll:
            return
        
        print(InfoFormatter.TreeInfoStart(),file=logFile)
        
        if len(self.infoList) != 0:
            for info in self.infoList:
                print(InfoFormatter.InfoItem(info),file=logFile)
        else:
            print(InfoFormatter.InfoItem(InfoItem(InfoTypes.ErrNone(),"i")))
                
        print(InfoFormatter.TreeInfoEnd(),file=logFile)

class NodeInfo:
    name = ""
    ID = ""
    infoList = []
    errCount = 0
    warnCount = 0
    infoCount = 0
    
    def __init__(self,nodeName,nodeID = "Unknown"):
        self.name = nodeName
        self.ID = nodeID
        self.infoList = []
        self.errCount = 0
        self.warnCount = 0
        self.infoCount = 0
        
    def AddInfo(self,newItem):
        if newItem.type == "e":
            self.errCount += 1
        elif newItem.type == "w":
            self.warnCount += 1
        elif newItem.type == "i":
            self.infoCount += 1
            
        self.infoList.append(newItem)
    
    def Print(self,writeAll = False, logFile = None):
        
        if len(self.infoList) == 0 and not writeAll:
            return
        
        print(InfoFormatter.NodeInfoStart(self.name,self.ID),file=logFile)
        
        if len(self.infoList) != 0:
            for info in self.infoList:
                print(InfoFormatter.InfoItem(info),file=logFile)
        else:
            print(InfoFormatter.InfoItem(InfoItem(InfoTypes.ErrNone(),"i")))
                
        print(InfoFormatter.NodeInfoEnd(),file=logFile)
        

def ShowInfoBox(message,title = "",icon = 'INFO'):
    def draw(self,context):
        self.layout.label(text = message)
    bpy.context.window_manager.popup_menu(draw,title = title,icon = icon)

def Validate(self,context):
    nodeTree = context.space_data.node_tree
    
    infoList = []
    
    if len(nodeTree.nodes) == 0:
        newTreeInfo = TreeInfo()
        newTreeInfo.AddInfo(InfoItem("there are no nodes in the node tree"))
        infoList.append(newTreeInfo)
    
    for link in nodeTree.links:
        if not link.is_valid:
            newTreeInfo = TreeInfo()
            newTreeInfo.AddInfo(InfoItem("there are invalid socket links in the node tree"))
            infoList.append(newTreeInfo)
    
    # errorList = []
    
    print(nodeTree.nodes)
    for node in nodeTree.nodes:
        if node.bl_idname in ["MCFG_N_Skeleton","MCFG_N_SkeletonPredef"] and node.exportClass:
            newInfo = node.Validate()
            infoList += newInfo
            
    return infoList
    
def ProcessNodeTree(context):
    
    CfgSkelly = Data.CfgSkeletons()
    CfgMesh = Data.CfgModels()
    
    nodeTree = context.space_data.node_tree
    
    for node in nodeTree.nodes:
        if node.export_type == "skeleton" and node.exportClass:
            newSkeleton = node.process()
            
            CfgSkelly.AddSkeleton(newSkeleton)
        
        if node.export_type == "model" and node.exportClass:
            newModel = node.process()
            CfgMesh.AddModel(newModel)
    
    
    
    return [CfgSkelly,CfgMesh]
    
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

def ExportFile(self,context,export = True):
    
    # Do tree validation
    
    if not os.path.exists(context.scene.modelCfgExportDir) and export:
        ShowInfoBox("No valid file location was specified","Error",'ERROR')
        self.report({'ERROR'},"No valid output location was given for model.cfg export")
        return
        
    nodeTree = context.space_data.node_tree
    
    if len(nodeTree.nodes) == 0:
        ShowInfoBox("There are no nodes in the tree",title = "Info",icon = 'INFO')
        return
        
    
    for link in nodeTree.links:
        if not link.is_valid:
            ShowInfoBox("There are invalid links in the tree",title = "Error",icon = 'ERROR')
            return
            
    
    [CfgSkelly,CfgMesh] = ProcessNodeTree(context)
    
    couldSortSkelly = CfgSkelly.SortParenting()
    couldSortMesh = CfgMesh.SortParenting()
    
    if not couldSortSkelly or not couldSortMesh:
        ShowInfoBox("Couldn't sort parenting",title = "Error",icon = 'ERROR')
        return
        
    
    [isValidData,counts] = ValidateClassStructure(CfgSkelly,CfgMesh)
    if not isValidData:
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
    
    if not isValidData or not export:
        return
        
    exportFile = open(context.scene.modelCfgExportDir + "model.cfg","w")
    
    print(CfgSkelly.Print(),file=exportFile)
    print(CfgMesh.Print(),file=exportFile)
    
    exportFile.close()