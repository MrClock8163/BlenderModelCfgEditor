import bpy
from bpy.types import Node
from . import n_tree
from . import utility
from .utility import NodeInfo, InfoItem, InfoTypes
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_ModelPresetArmaman(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Model class node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Model class - ArmaMan"
    # Icon identifier
    bl_icon = 'OBJECT_DATA'
    
    node_group = "model"
    export_type = "model"
    
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

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: ArmaMan")

    # Detail buttons in the sidebar.
    # If this function is not defined, the draw_buttons function is used instead
    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.prop(self, "exportClass")
        box.label(text="Name: ArmaMan")

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
        

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Model preset"