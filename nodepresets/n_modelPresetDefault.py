import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_ModelPresetDefault(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Model class node'''
    
    # Mandatory variables
    bl_label = "Model class - Default"
    bl_icon = 'OBJECT_DATA'
    
    # Custom variables
    node_group = "model"
    process_type = "model"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Model-class:-Default"
    
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
        if len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
        
        if len(self.outputs[0].links) > 0:
            self.exportClass = True
        
    def init(self, context):
        self.customColor()
        
        self.outputs.new('MCFG_S_ModelParent', "Out")

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.label(text="Name: Default")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "exportClass")
        box.label(text="Name: Default")
        
    # Custom functions
    def getModelName(self):
        return "Default"
    
    def process(self):        
        return Presets.DefaultModel()
        
    def inspect(self):
        data = self.process()
        print(data.Print())