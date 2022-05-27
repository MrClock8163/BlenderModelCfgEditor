import bpy
from bpy.types import Node
from . import n_tree

class MCFG_N_ValueString(Node, n_tree.MCFG_N_Base):
    # Description string
    '''String input node'''
    
    # Mandatory variables
    bl_label = "String input"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "value"
    
    # Node properties
    stringProperty: bpy.props.StringProperty(
        name = "Value",
        default = ""
    )
    
    # Standard functions
    def draw_label(self):
        return "String"
        
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ValueString', "Value")

    def draw_buttons(self, context, layout):
        layout.prop(self, "stringProperty")
        
    # Custom functions
    def process(self):
        return self.stringProperty.strip()