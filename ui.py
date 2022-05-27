import bpy
from . import utility
import os
            
class MCFG_ReportBox(bpy.types.Operator):
    # Description string
    '''Info report pop-up'''
    
    # Mandatory variables
    bl_label = "Report"
    bl_idname = "mcfg.reportbox"
    
    # Operator properties
    report = bpy.props.StringProperty (
        name = "Report info",
        description = "Pop-up text to display",
        default = ""
    )
    
    # Standard functions
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
    # Description string
    """Model.cfg export operator"""
    
    # Mandatory variables
    bl_idname = "mcfg.export"
    bl_label = "Export config"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        
    def execute(self,context):
        utility.ExportFile(self,context)
        
        return {'FINISHED'}
        
class MCFG_Panel_Validate(bpy.types.Operator):
    # Description string
    """Model.cfg validator operator"""
    
    # Mandatory variables
    bl_idname = "mcfg.validate"
    bl_label = "Validate setup"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        
    def execute(self,context):
        utility.ExportFile(self,context,False)
        return {'FINISHED'}

class MCFG_PT_Panel(bpy.types.Panel):
    # Description string
    '''Addon side panel'''
    
    # Mandatory variables
    bl_label = "Node tree"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Model config"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'NODE_EDITOR' and context.space_data.tree_type == 'MCFG_N_Tree'
    
    def draw(self, context):
        tree = context.space_data.node_tree
        
        if tree:
            layout = self.layout
            layout.label(text="Export configuration")
            layout.operator('mcfg.validate', icon = 'FILE_REFRESH')
            layout.prop(context.scene,"modelCfgExportDir")
            layout.operator('mcfg.export', icon = 'EXPORT')

# Replace node editor header to include custom operators
def draw_header(self,context):
    if context.space_data.type == 'NODE_EDITOR' and context.space_data.tree_type == 'MCFG_N_Tree' and context.space_data.node_tree is not None:
        layout = self.layout
        layout.separator()        
        layout.operator('mcfg.validate', icon = 'FILE_REFRESH', text = "")
        layout.prop(context.scene,"modelCfgExportDir",text = "")
        layout.operator('mcfg.export', icon = 'EXPORT', text = "")