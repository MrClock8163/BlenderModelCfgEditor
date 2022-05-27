import bpy
from bpy.types import Node
from . import n_tree
from . import utility_presets as Presets

class MCFG_N_ModelPresetArmaman(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Model class node'''
    
    # Mandatory variables
    bl_label = "Model class - ArmaMan"
    bl_icon = 'OBJECT_DATA'
    
    # Custom variables
    node_group = "model"
    export_type = "model"
    
    # Side panel properties
    def updateExportClass(self,context):
        if len(self.inputs) != 1:
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
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
        
        if len(self.outputs[0].links) > 0:
            self.exportClass = True
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_SkeletonParent', "Skeleton")
        self.inputs.new('MCFG_S_ModelSectionList', "Sections")
        self.outputs.new('MCFG_S_ModelParent', "Out")

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.label(text="Name: ArmaMan")
        
    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "exportClass")
        box.label(text="Name: ArmaMan")
        
    # Custom functions
    def getSkeleton(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getSkeletonName()
        
    def getModelName(self):
        return "ArmaMan"
        
    def getNewSections(self):
        if len(self.inputs[1].links) == 0:
            return []
            
        sectionList = self.inputs[1].links[0].from_node.process()
        
        return sectionList
        
    def process(self):        
        return Presets.ArmaMan(self.getSkeleton(),self.getNewSections())