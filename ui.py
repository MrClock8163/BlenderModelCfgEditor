import bpy
from . import utility
import os

class MCFG_InfoBox(bpy.types.Operator):
    """Shows info message"""
    bl_idname = "mcfg.infobox"
    bl_label = "Info"
    
    infotext = bpy.props.StringProperty(
        name = "infotext",
        description = "infotext",
        default = "Some text"
    )
    
    def execute(self,context):
        return {'FINISHED'}
        
    def invoke(self,context,event):
        return context.window_manager.invoke_props_dialog(self,width = 750)
        
    def draw(self,context):
        layout = self.layout
        
        
        for line in self.infotext.split("|"):
            layout.label(text = line)
            
class MCFG_ReportBox(bpy.types.Operator):
    bl_label = "Report"
    bl_idname = "mcfg.reportbox"
    
    report = bpy.props.StringProperty (
        name = "Report info",
        description = "Pop-up text to display",
        default = ""
    )
    
    def draw(self,context):
        layout = self.layout
        sections = self.report.split("|")
        
        for section in sections:
            box = layout.box()
            for line in section.split(","):
                box.label(text=line)
    
    def execute(self,context):
        return {'FINISHED'}
        
    def invoke(self,context,event):
        return context.window_manager.invoke_props_dialog(self)

class MCFG_Panel_Export(bpy.types.Operator):
    """Exports the node tree setup into a model.cfg file"""
    bl_idname = "mcfg.export"
    bl_label = "Export config"
    
    @classmethod
    def poll(cls, context):
        return context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        
    def execute(self,context):
        
        utility.ExportFile(self,context)
        
        return {'FINISHED'}
        
class MCFG_Panel_Validate(bpy.types.Operator):
    """Validates the node tree"""
    bl_idname = "mcfg.validate"
    bl_label = "Validate setup"
    
    @classmethod
    def poll(cls, context):
        return context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        
    def execute(self,context):
        utility.ExportFile(self,context,False)
        return {'FINISHED'}
        
        infoList = utility.Validate(self,context)
        
        addonPrefs = bpy.context.preferences.addons[__package__].preferences
        outputTarget = addonPrefs.validationOutput
        writeAll = addonPrefs.writeAll
        
        outputFile = None
        outputPath = context.scene.modelCfgExportDir
        if outputTarget == 'FILE' and os.path.exists(outputPath):
            outputPath += "model.cfg.valid.log"
            outputFile = open(outputPath,"w")
        
        warnCount = 0
        errCount = 0
        infoCount = 0
        
        for item in infoList:
            item.Print(writeAll,outputFile)
            warnCount += item.warnCount
            errCount += item.errCount
            infoCount += item.infoCount
            
        if addonPrefs.warnsAreErr:
            errCount += warnCount
        
        
        # FIGURE OUT HOW TO DISPLAY THE NOTIFICATION
        if errCount > 0:
            self.report({'ERROR'},"Node tree validation has failed")
            outputName = "system console"
            if outputFile is not None:  
                outputName = "log file"
            # utility.ShowInfoBox("See the " + outputName + " for further information","Invalid node tree",'ERROR')
        else:
            self.report({'INFO'},"Node tree validation has succeeded")
        
        # self.report({'INFO'},resultShort)
        # bpy.ops.mcfg.infobox('INVOKE_DEFAULT',infotext = result)
        
        return {'FINISHED'}

class MCFG_PT_Panel(bpy.types.Panel):
    # bl_idname = "MCFG_PT_Panel"
    bl_label = "Node tree"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Model config"
    
    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'NODE_EDITOR' and context.space_data.tree_type == 'MCFG_N_Tree'
    
    exportDirPath: bpy.props.StringProperty(
        # name = "Export path",
        # description = "Directory to save file to",
        # default = "",
        # subtype = 'FILE_PATH'
    )
    
    def draw(self, context):
        tree = context.space_data.node_tree
        
        if tree:
            layout = self.layout
            layout.label(text="Export configuration")
            layout.operator('mcfg.validate', icon = 'FILE_REFRESH')
            layout.prop(context.scene,"modelCfgExportDir")
            layout.operator('mcfg.export', icon = 'EXPORT')

def draw_header(self,context):
    if context.space_data.type == 'NODE_EDITOR' and context.space_data.tree_type == 'MCFG_N_Tree' and context.space_data.node_tree is not None:
        layout = self.layout
        layout.separator()        
        layout.operator('mcfg.validate', icon = 'FILE_REFRESH', text = "")
        layout.prop(context.scene,"modelCfgExportDir",text = "")
        layout.operator('mcfg.export', icon = 'EXPORT', text = "")