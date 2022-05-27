import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_ModelPresetCopy(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Model class node'''
    
    # Mandatory variables
    bl_label = "Model class - copy"
    bl_icon = 'OBJECT_DATA'
    
    # Custom variables
    node_group = "model"
    export_type = "model"
    
    # Node properties
    modelName: bpy.props.StringProperty(
        default="Model",
        name="Name",
        description = "Name of the model class\nNaming rules:\n-must be same as the name of the model P3D file\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    
    # Side panel properties
    def updateExportClass(self,context):
        if len(self.outputs) != 1:
            return
        
        if not self.exportClass:
            if len(self.outputs[0].links) > 0:
                for i in range(len(self.outputs[0].links)):
                    self.outputs[0].id_data.links.remove(self.outputs[0].links[0])
                self.exportClass = False
                
    exportClass: bpy.props.BoolProperty(
        default = True,
        name = "Export",
        description = "Include this class in the exported config",
        update = updateExportClass
    )
    
    # Standard functions
    def draw_label(self):
        return "Model preset"
        
    def update(self):
        self.unlinkInvalidSockets()
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelParent', "Parent")
        self.outputs.new('MCFG_S_ModelParent', "Out")

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.label(text="Name: copy class")
        box.prop(self, "modelName")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "exportClass")
        box.label(text="Name: copy class")
        box.prop(self, "modelName")
        
    # Custom functions
    def getModelName(self):
        return self.modelName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getModelName()
    
    def process(self):        
        return Presets.CloneModel(self.getModelName(),self.getParentName())