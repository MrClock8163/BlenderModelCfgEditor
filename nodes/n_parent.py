import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data

class MCFG_N_Parent(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Internal dummy parent node'''
    
    # Mandatory variables
    bl_label = "Dummy parent"
    bl_icon = 'FILE_PARENT'
    
    # Custom variables
    node_group = "operator"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Parent"
    
    # Node properties
    name: bpy.props.StringProperty(
        default="Parent",
        name="Name",
        description = "Name of the dummy parent"
    )
    
    # Standard functions
    def draw_label(self):
        return "Parent"
        
    def init(self, context):
        self.customColor()
        
        self.outputs.new('MCFG_S_Universal', "Out")

    def draw_buttons(self, context, layout):
        layout.prop(self, "name")
        
    # Custom functions
    def getBoneName(self):
        return self.name.strip()
        
    def getSkeletonName(self):
        return self.name.strip()
        
    def getModelName(self):
        return self.name.strip()
        
    def getAnimName(self):
        return self.name.strip()
        
    def inspect(self):
        print(self.name.strip())