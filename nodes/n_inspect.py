import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data

class MCFG_N_Inspect(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Data inspector node'''
    
    # Mandatory variables
    bl_label = "Data inspector"
    bl_icon = 'VIEWZOOM'
    
    # Custom variables
    node_group = "operator"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Data-inspector"
    
    # Node properties
    active: bpy.props.BoolProperty(
        name = "Active",
        default = True
    )
    name: bpy.props.StringProperty(
        name = "Name",
        description = "Identifier of inspector node",
        default = ""
    )
    
    # Standard functions
    def draw_label(self):
        return "Inspector"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_Universal', "Value")

    def draw_buttons(self, context, layout):
        layout.prop(self,"name")
        layout.prop(self,"active")
        
    # Custom functions
    def inspect(self):
        if len(self.inputs[0].links) != 1 or not self.active:
            return
            
        print("==== Inspector output (ID: " + self.name.strip() + ") ====")
        self.inputs[0].links[0].from_node.inspect()