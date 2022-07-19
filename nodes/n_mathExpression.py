import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility as Utils

class MCFG_N_MathExpression(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Math expression node'''
    
    # Mandatory variables
    bl_label = "Simple expression"
    bl_icon = 'FILE_SCRIPT'
    
    # Custom variables
    node_group = "operator"
    doc_url = ""
    
    # Node properties
    expression: bpy.props.StringProperty(
        name = "Expression",
        description = "Simple python expression that returns an integer or floating point number (preferably only simple math operators such as ()+-/*^)",
        default = ""
    )
    isDeg: bpy.props.BoolProperty(
        name = "Deg",
        default = False,
        description = "The result value is an angle, and is in degrees units"
    )
    
    # Standard functions
    def draw_label(self):
        return "Simple expression"
        
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
        split.prop(self, "expression",text="")
        
    # Custom functions
    def process(self):
        expression = self.expression.strip()
        returnValue = 0
        
        try:
            eval(expression)
        except:
            pass
        else:
            returnValue = eval(expression)
    
        return Utils.FloatValue(returnValue,self.isDeg)
        
    def inspect(self):
        print(self.process())