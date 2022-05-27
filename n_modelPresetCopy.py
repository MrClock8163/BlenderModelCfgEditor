import bpy
from bpy.types import Node
from . import n_tree
from . import utility
from .utility import NodeInfo, InfoItem, InfoTypes
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_ModelPresetCopy(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Model class node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Model class - copy"
    # Icon identifier
    bl_icon = 'OBJECT_DATA'
    
    node_group = "model"
    export_type = "model"
    
    def updateExportClass(self,context):
        if len(self.outputs) != 1:
            return
        
        if not self.exportClass:
            if len(self.outputs[0].links) > 0:
                for i in range(len(self.outputs[0].links)):
                    self.outputs[0].id_data.links.remove(self.outputs[0].links[0])
                self.exportClass = False
    
    modelName: bpy.props.StringProperty(
        default="Model",
        name="Name",
        description = "Name of the model class\nNaming rules:\n-must be same as the name of the model P3D file\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    
    exportClass: bpy.props.BoolProperty(
        default = True,
        name = "Export",
        description = "Include this class in the exported config",
        update = updateExportClass
    )
    
    def update(self):
        self.unlinkInvalidSockets()
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelParent', "Parent")
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
        box.label(text="Name: copy class")
        box.prop(self, "modelName")

    # Detail buttons in the sidebar.
    # If this function is not defined, the draw_buttons function is used instead
    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.prop(self, "exportClass")
        box.label(text="Name: copy class")
        box.prop(self, "modelName")
        
    def getModelName(self):
        return self.modelName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getModelName()
    
    def process(self):        
        return Presets.CloneModel(self.getModelName(),self.getParentName())
        

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Model preset"