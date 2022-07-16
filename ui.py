import os
import json
import bpy
from bpy_extras.io_utils import ImportHelper
from . import utility
from . import utility_presets_setup as Presets
from . import bl_info
from . import utility_import

class MCFG_MT_TemplatesNodeScript(bpy.types.Menu):
    # Description string
    '''Node script templates menu'''
    
    # Mandatory variables
    bl_label = "Custom node script"
    
    # Standard functions
    def draw(self,context):
        layout = self.layout
        
        templateDir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"templates")
        
        templatesFile = open(os.path.join(templateDir,"templates.json"),"r")
        templates = json.load(templatesFile)
        templatesFile.close()
        
        if len(templates) == 0:
            layout.lable(text="No templates are available")
            return
            
        for key in templates.keys():
            name = templates.get(key).get("name")
            path = templates.get(key).get("file")
            layout.operator('text.open',text=name).filepath = os.path.join(templateDir,path)

class MCFG_MT_TemplatesSetupPresets(bpy.types.Menu):
    # Description string
    '''Node setup templates menu'''
    
    # Mandatory variables
    bl_label = "Setup preset"
    
    # Standard functions
    def draw(self,context):
        layout = self.layout
        
        presets = Presets.PresetDefinitions()
        
        for preset in presets:
            layout.operator('text.open',text=preset.get("name")).filepath = preset.get("path")

class MCFG_GT_ModelSelectionItem(bpy.types.PropertyGroup):
    # Description string
    '''Model selection list item'''
    
    # Properties
    name: bpy.props.StringProperty(
        name = "Name",
        description = "Selection name",
        default = "Untitled selection"
    )
    include: bpy.props.BoolProperty(
        name = "Include",
        description = "",
        default = False
    )

class MCFG_GT_NodeSetupPresetItem(bpy.types.PropertyGroup):
    # Description string
    '''Setup preset list item'''
    
    # Properties
    name: bpy.props.StringProperty(
        name = "Name",
        description = "Name of the preset",
        default = "Untitled preset"
    )
    desc: bpy.props.StringProperty(
        name = "Description",
        description = "Description of the preset",
        default = ""
    )
    custom: bpy.props.BoolProperty(
        name = "Custom",
        description = "Whether the preset is custom or built-in",
        default = False
    )
    path: bpy.props.StringProperty(
        name = "Path",
        description = "Path to preset file",
        default = ""
    )

class MCFG_UL_ModelSelectionList(bpy.types.UIList):
    # Description string
    '''Model selection list'''
    
    # Standard functions
    def draw_item(self,context,layout,data,item,icon,active_data,active_propname,index):
        if self.layout_type in {'DEFAULT','COMPACT'}:
            layout.prop(item,"include",text = "")
            layout.label(text=item.name)
        
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.prop(item,"include",text = "")
            layout.label(text=item.name)

class MCFG_UL_NodeSetupPresetList(bpy.types.UIList):
    # Description string
    '''Node setup preset list'''
    
    # Standard functions
    def draw_item(self,context,layout,data,item,icon,active_data,active_propname,index):
        icon = 'OUTLINER_OB_GROUP_INSTANCE'
        if item.custom:
            icon = 'FILE_FOLDER'
        if self.layout_type in {'DEFAULT','COMPACT'}:
            layout.label(text=item.name,icon=icon)
        
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text=item.name,icon=icon)

class MCFG_OT_BonesFromModel(bpy.types.Operator):
    # Description string
    '''Create bones from model selections'''
    
    # Mandatory variables
    bl_label = "Bones"
    bl_idname = "mcfg.bonesfrommodel"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        isNodeTree = context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        hasSelected = len(bpy.context.selected_objects) == 1 and bpy.context.selected_objects[0].type == 'MESH'
        return (isNodeTree and hasSelected)
        
    def draw(self,context):
        layout = self.layout
        layout.template_list("MCFG_UL_ModelSelectionList","SelectionList",context.scene,"MCFG_SP_ModelSelectionList",context.scene,"MCFG_SP_ModelSelectionListIndex")
        layout.prop(context.scene,"MCFG_SP_ModelSelectionListListNode")
    
    def execute(self,context):
        utility.CreateBoneNodes(self,context)
        return {'FINISHED'}
        
    def invoke(self,context,event):
        selectedObject = bpy.context.selected_objects[0]
        
        bpy.context.scene.MCFG_SP_ModelSelectionList.clear()
        
        # populate list with vertex groups from selected mesh
        for group in selectedObject.vertex_groups:
            newItem = bpy.context.scene.MCFG_SP_ModelSelectionList.add()
            newItem.name = group.name

        return context.window_manager.invoke_props_dialog(self)

class MCFG_OT_SectionsFromModel(bpy.types.Operator):
    # Description string
    '''Create sections from model selections'''
    
    # Mandatory variables
    bl_label = "Sections"
    bl_idname = "mcfg.sectionsfrommodel"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        isNodeTree = context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        hasSelected = len(bpy.context.selected_objects) == 1 and bpy.context.selected_objects[0].type == 'MESH'
        return (isNodeTree and hasSelected)
        
    def draw(self,context):
        layout = self.layout
        layout.template_list("MCFG_UL_ModelSelectionList","SelectionList",context.scene,"MCFG_SP_ModelSelectionList",context.scene,"MCFG_SP_ModelSelectionListIndex")
    
    def execute(self,context):
        utility.CreateSectionNodes(self,context)
        return {'FINISHED'}
        
    def invoke(self,context,event):
        selectedObject = bpy.context.selected_objects[0]
        
        bpy.context.scene.MCFG_SP_ModelSelectionList.clear()
        
        # populate list with vertex groups from selected mesh
        for group in selectedObject.vertex_groups:
            newItem = bpy.context.scene.MCFG_SP_ModelSelectionList.add()
            newItem.name = group.name

        return context.window_manager.invoke_props_dialog(self)

class MCFG_OT_ReportBox(bpy.types.Operator):
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

class MCFG_OT_Import(bpy.types.Operator,ImportHelper):
    # Description string
    """Import model.cfg and create nodes"""
    
    # Mandatory variables
    bl_idname = "mcfg.import"
    bl_label = "Import config"
    
    # Custom properties
    filter_glob: bpy.props.StringProperty(
        default = '*.cfg',
        options = {'HIDDEN'}
    )
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        isNodeTree = context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        hasArmaTools = os.path.isdir(bpy.context.preferences.addons[__package__].preferences.armaToolsFolder)
        return isNodeTree and hasArmaTools
        
    def execute(self,context):
              
        if os.path.split(self.filepath)[1] != "model.cfg":
            utility.ShowInfoBox("Selected file is not model config","Error",'ERROR')
            return {'FINISHED'}
        
        utility_import.ImportFile(self,context)
        
        return {'FINISHED'}

class MCFG_OT_Export(bpy.types.Operator):
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
        
class MCFG_OT_Validate(bpy.types.Operator):
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

class MCFG_OT_LoadPresets(bpy.types.Operator):
    # Description string
    """Load node setup presets"""
    
    # Mandatory variables
    bl_idname = "mcfg.loadpresets"
    bl_label = "Load/Reload presets"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        
    def execute(self,context):
        Presets.ReloadPresets()
        return {'FINISHED'}

class MCFG_OT_InsertPreset(bpy.types.Operator):
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
        Presets.ReloadPresets()
        
        if context.scene.MCFG_SP_PresetListIndex not in range(len(context.scene.MCFG_SP_PresetList)):
            return {'FINISHED'}
        
        preset = context.scene.MCFG_SP_PresetList[context.scene.MCFG_SP_PresetListIndex]
        
        if not os.path.isfile(preset.get("path")):
            utility.ShowInfoBox("Preset not found","Error",'ERROR')
            return {'FINISHED'}
        
        Presets.InsertPreset(self,context,preset.get("path"))
        
        return {'FINISHED'}

class MCFG_OT_CreatePreset(bpy.types.Operator):
    # Description string
    """Create node setup preset from current node tree"""
    
    # Mandatory variables
    bl_idname = "mcfg.createpreset"
    bl_label = "New custom preset"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        isNodeTree = context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        hasFolder = os.path.isdir(bpy.context.preferences.addons[__package__].preferences.customSetupPresets)
        return (isNodeTree and hasFolder)
    
    def draw(self,context):
        layout = self.layout
        layout.prop(context.scene,"MCFG_SP_PresetName")
        layout.prop(context.scene,"MCFG_SP_PresetDesc")
    
    def execute(self,context):
        Presets.CreatePreset(self,context)
        Presets.ReloadPresets()
        return {'FINISHED'}
        
    def invoke(self,context,event):    
        Presets.ReloadPresets()
        
        context.scene.MCFG_SP_PresetName = "Untitled preset"
        context.scene.MCFG_SP_PresetDesc = ""
        
        if len(context.space_data.node_tree.nodes) == 0:
            utility.ShowInfoBox("There are no nodes in the tree","Info",'INFO')
            return {'FINISHED'}
        
        for link in context.space_data.node_tree.links:
            if not link.is_valid:
                utility.ShowInfoBox("There are invalid links in the tree","Error",'ERROR')
                return {'FINISHED'}

        return context.window_manager.invoke_props_dialog(self)
        
class MCFG_OT_DeletePreset(bpy.types.Operator):
    # Description string
    """Delete selected preset"""
    
    # Mandatory variables
    bl_idname = "mcfg.deletepreset"
    bl_label = "Delete custom preset"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        isNodeTree = context.space_data.type == "NODE_EDITOR" and context.space_data.tree_type == "MCFG_N_Tree"
        hasFolder = os.path.isdir(bpy.context.preferences.addons[__package__].preferences.customSetupPresets)
        return (isNodeTree and hasFolder)
    
    preset: bpy.props.StringProperty(
        name = "Preset",
        description = "",
        default = ""
    )
    
    def draw(self,context):
        layout = self.layout
        layout.label(text="Are you sure you want to delete this preset?")
        layout.label(text=self.preset)
    
    def execute(self,context):
        
        path = context.scene.MCFG_SP_PresetList[context.scene.MCFG_SP_PresetListIndex].path
        Presets.DeletePreset(path)
        
        return {'FINISHED'}
        
    def invoke(self,context,event):
        Presets.ReloadPresets()
        
        
        selectionIndex = context.scene.MCFG_SP_PresetListIndex
        if selectionIndex not in range(len(context.scene.MCFG_SP_PresetList)):
            return {'FINISHED'}
        
        path = context.scene.MCFG_SP_PresetList[selectionIndex].path
        
        if not os.path.isfile(path):
            utility.ShowInfoBox("Preset not found","Error",'ERROR')
            return {'FINISHED'}
        
        preset = Presets.ReadPresetFile(path)
        
        if not preset.get("custom"):
            utility.ShowInfoBox("Built-in presets cannot be deleted","Info",'INFO')
            return {'FINISHED'}

        self.preset = "Name: " + preset.get("name")

        return context.window_manager.invoke_props_dialog(self)

class MCFG_OT_Inspect(bpy.types.Operator):
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

class MCFG_PT_Tools(bpy.types.Panel):
    # Description string
    '''Tools panel section'''
    
    # Mandatory variables
    bl_label = "Tools"
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
            box.label(text="Mesh:")
            box.operator('mcfg.bonesfrommodel', icon = 'BONE_DATA',text="Bones from model")
            box.operator('mcfg.sectionsfrommodel', icon = 'MESH_DATA',text="Sections from model")
            layout.separator()
            box = layout.box()
            box.label(text="Inspection:")
            box.operator('mcfg.inspect', icon = 'VIEWZOOM')

class MCFG_PT_Import(bpy.types.Panel):
    # Description string
    '''Import panel section'''
    
    # Mandatory variables
    bl_label = "Import"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Model config"
    
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'NODE_EDITOR' and context.space_data.tree_type == 'MCFG_N_Tree'
    
    def draw_header(self,context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("wm.url_open", text="", icon='HELP').url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Import"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.alert = os.path.isdir(bpy.context.preferences.addons[__package__].preferences.armaToolsFolder)
        row.label(text="Read the documentation",icon='ERROR')
        box = layout.box()
        box.label(text="Links:")
        box.prop(context.scene,"MCFG_SP_ImportLinkDepth",expand=True)
        box.label(text="Data:")
        box.prop(context.scene,"MCFG_SP_ImportDepth",expand=True)
        layout.operator('mcfg.import', icon = 'IMPORT')
        
        box.enabled = os.path.isdir(bpy.context.preferences.addons[__package__].preferences.armaToolsFolder)

class MCFG_PT_Export(bpy.types.Panel):
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
    
    def draw_header(self,context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("wm.url_open", text="", icon='HELP').url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Validation-and-export"
    
    def draw(self, context):
        tree = context.space_data.node_tree
        
        if tree:
            layout = self.layout
            layout.operator('mcfg.validate', icon = 'CHECKMARK')
            layout.separator()
            box = layout.box()
            box.label(text="Settings:")
            row = box.row(align=True)
            row.alert = not os.path.isdir(context.scene.MCFG_SP_ExportDir)
            row.label(text="Directory:")
            row.prop(context.scene,"MCFG_SP_ExportDir",text="")
            col = box.column(align=True)
            row = col.row(align=True)
            row.alert = utility.EnumBoolGet(context.scene.MCFG_SP_IgnoreErrors)
            row.label(text="Ignore errors:")
            row.prop(context.scene,"MCFG_SP_IgnoreErrors",expand=True)
            row = col.row(align=True)
            row.label(text="Open file:")
            row.prop(context.scene,"MCFG_SP_OpenFile",expand=True)
            layout.operator('mcfg.export', icon = 'EXPORT')

class MCFG_PT_Presets(bpy.types.Panel):
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
    
    def draw_header(self,context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("wm.url_open", text="", icon='HELP').url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node-setup-presets"
    
    def draw(self, context):
        tree = context.space_data.node_tree
        
        if tree:
            layout = self.layout
            layout.template_list("MCFG_UL_NodeSetupPresetList","NodePresetList",context.scene,"MCFG_SP_PresetList",context.scene,"MCFG_SP_PresetListIndex")
            column_flow = layout.column_flow(columns = 4,align=True)
            column_flow.operator('mcfg.addpreset', icon = 'PASTEDOWN',text = "")
            column_flow.operator('mcfg.loadpresets', icon = 'FILE_REFRESH',text = "")
            column_flow.operator('mcfg.createpreset', icon = 'ADD',text = "")
            column_flow.operator('mcfg.deletepreset', icon = 'REMOVE',text = "")
            
            selectionIndex = context.scene.MCFG_SP_PresetListIndex
            if selectionIndex in range(len(context.scene.MCFG_SP_PresetList)):
                row = layout.row()
                item = context.scene.MCFG_SP_PresetList[selectionIndex]
                row.prop(item,"desc",text="")
                row.enabled = False
            
            return

class MCFG_PT_Docs(bpy.types.Panel):
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
        layout = self.layout
        wiki = layout.operator('wm.url_open', text = "Open addon wiki",icon='URL')
        wiki.url = bl_info.get("doc_url")
        layout.separator()
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
        layout.operator('mcfg.validate', icon = 'CHECKMARK', text = "")
        layout.prop(context.scene,"MCFG_SP_ExportDir",text = "")
        layout.operator('mcfg.export', icon = 'EXPORT', text = "")

# Add addon related templates to the script templates menu
def draw_menu(self,context):
    layout = self.layout
    layout.separator()
    layout.label(text="Arma 3 model config editor")
    layout.menu("MCFG_MT_TemplatesNodeScript")
    layout.menu("MCFG_MT_TemplatesSetupPresets")