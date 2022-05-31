import bpy
from bpy.types import NodeSocket

class MCFG_S_ValueBool(NodeSocket):
    # Description string
    '''Bool socket'''
    
    # Mandatory variables
    bl_label = "Bool value"
    
    # Custom variables
    compatibleSockets = []
    
    # Socket properties
    boolValue: bpy.props.BoolProperty(
        name="Value",
        default=True
    )
    
    # Standard functions
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "boolValue", text=text)

    def draw_color(self, context, node):
        return (1, 1, 0, 1.0)
        
    # Custom functions
    def getValue(self):
        return self.boolValue