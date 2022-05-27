import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_ValueFloat(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Float input node'''
    
    # Mandatory variables
    bl_label = "Float input"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "value"
    
    # Node properties
    floatProperty: bpy.props.FloatProperty(
        name = "Value",
        default = 0.0,
        min = -100,
        max = 100,
        soft_max = 50,
        soft_min = -50
    )
    
    # Standard functions
    def draw_label(self):
        return "Float"
        
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ValueFloat', "Value")

    def draw_buttons(self, context, layout):
        layout.prop(self, "floatProperty")
        
    # Custom functions
    def process(self):
        return self.floatProperty