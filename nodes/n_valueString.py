import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_ValueString(Node, n_tree.MCFG_N_Base):
    # Description string
    '''String input node'''
    
    # Mandatory variables
    bl_label = "String input"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "operator"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-String-input"
    
    # Node properties
    stringValue: bpy.props.StringProperty(
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
        layout.prop(self, "stringValue")
        
    # Custom functions
    def process(self):
        return self.stringValue.strip()
        
    def inspect(self):
        print(self.process())