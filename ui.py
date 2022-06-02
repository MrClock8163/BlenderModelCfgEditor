import os
import webbrowser
import bpy
from . import utility
from . import utility_presets_setup as Presets
from . import bl_info
            
class MCFG_ReportBox(bpy.types.Operator):
    # Description string
    '''Info report pop-up'''
    
    # Mandatory variables
    bl_label = "Report"
    bl_idname = "mcfg.reportbox"
    
    # Operator properties
    report: bpy.props.StringProperty (
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
    """Export node setup to model.cfg format"""
    
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
    """Validate the processed node setup data"""
    
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
        
class MCFG_Panel_AddPreset(bpy.types.Operator):
    # Description string
    """Insert node setup preset into current node tree"""
    
    # Mandatory variables
    bl_idname = "mcfg.addpreset"
    bl_label = "Insert preset"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        
    def execute(self,context):
        Presets.AddSetup(self,context,context.scene.modelCfgEditorSetupPresets)
        return {'FINISHED'}

class MCFG_Panel_Inspect(bpy.types.Operator):
    # Description string
    """Print the output data of the inspected nodes to the system console"""
    
    # Mandatory variables
    bl_idname = "mcfg.inspect"
    bl_label = "Inspect data"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        
    def execute(self,context):
        utility.InspectData(self,context)
        return {'FINISHED'}

class MCFG_PT_Panel_Inspect(bpy.types.Panel):
    # Description string
    '''Inspect panel section'''
    
    # Mandatory variables
    bl_label = "Inspect"
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
            layout.operator('mcfg.inspect', icon = 'VIEWZOOM')

class MCFG_PT_Panel_Export(bpy.types.Panel):
    # Description string
    '''Export panel section'''
    
    # Mandatory variables
    bl_label = "Export"
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
            layout.operator('mcfg.validate', icon = 'FILE_REFRESH')
            box = layout.box()
            box.label(text="Export configuration")
            box.prop(context.scene,"modelCfgExportDir")
            box.prop(context.scene,"modelCfgEditorIgnoreErrors")
            box.prop(context.scene,"modelCfgEditorOpenNotepad")
            layout.operator('mcfg.export', icon = 'EXPORT')

class MCFG_PT_Panel_Presets(bpy.types.Panel):
    # Description string
    '''Preset panel section'''
    
    # Mandatory variables
    bl_label = "Presets"
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
            box = layout.box()
            box.label(text="Node presets")
            box.prop(context.scene,"modelCfgEditorSetupPresets",text="")
            box.operator('mcfg.addpreset', icon = 'ADD')

class MCFG_PT_Panel_Docs(bpy.types.Panel):
    # Description string
    '''Documentation panel section'''
    
    # Mandatory variables
    bl_label = "Documentation"
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
            wiki = layout.operator('wm.url_open', text = "Open addon wiki",icon='URL')
            wiki.url = bl_info.get("doc_url")
            box = layout.box()
            box.label(text="Node documentation")
            op = box.operator('wm.url_open', text = "Open",icon='HELP')
            
            if len(context.selected_nodes) != 1:
                box.enabled = False
                return
            else:
                doc_url = context.selected_nodes[0].doc_url
                if doc_url == "":
                    box.enabled = False
                    return
                else:
                    op.url = doc_url

# Replace node editor header to include custom operators
def draw_header(self,context):
    if context.space_data.type == 'NODE_EDITOR' and context.space_data.tree_type == 'MCFG_N_Tree' and context.space_data.node_tree is not None:
        layout = self.layout
        layout.separator()        
        layout.operator('mcfg.validate', icon = 'FILE_REFRESH', text = "")
        layout.prop(context.scene,"modelCfgExportDir",text = "")
        layout.operator('mcfg.export', icon = 'EXPORT', text = "")