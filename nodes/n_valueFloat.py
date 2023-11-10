import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility as Utils

class MCFG_N_ValueFloat(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Float input node'''
    
    # Mandatory variables
    bl_label = "Float input"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "operator"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Float-input"
    
    # Node properties    
    floatValue: bpy.props.FloatProperty(
        name = "Value",
        default = 0.0,
        min = -10000,
        max = 10000,
        soft_max = 50,
        soft_min = -50
    )
    isDeg: bpy.props.BoolProperty(
        name = "Deg",
        default = False,
        description = "The value is an angle, and is in degrees units"
    )
    
    # Standard functions
    def draw_label(self):
        return "Float"
        
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ValueFloat', "Value")

    def draw_buttons(self, context, layout):
        split = layout.split(align=True,factor=0.2)
        if self.isDeg:
            icon = 'LAYER_USED'
        else:
            icon = 'BLANK1'
        split.prop(self, "isDeg",icon=icon)
        split.prop(self, "floatValue")
        
    # Custom functions
    def process(self):
        return Utils.FloatValue(self.floatValue,self.isDeg)
        
    def inspect(self):
        print(self.process())