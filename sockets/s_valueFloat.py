import bpy
from bpy.types import NodeSocket

class MCFG_S_ValueFloat(NodeSocket):
    # Description string
    '''Float socket'''
    
    # Mandatory variables
    bl_label = "Float value"
    
    # Custom variables
    compatibleSockets = []
    
    # Socket properties
    floatValue: bpy.props.FloatProperty(
        name = "Value",
        default = 0.0,
        min = -1000,
        max = 1000,
        soft_max = 100,
        soft_min = -100
    )
    isDeg: bpy.props.BoolProperty(
        name = "Deg",
        default = False,
        description = "The value is an angle, and is in degrees units"
    )
    
    # Standard functions
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            split = layout.split(align=True,factor = 0.2)
            if self.isDeg:
                icon = 'LAYER_USED'
            else:
                icon = 'BLANK1'
            split.prop(self, "isDeg",icon=icon)
            split.prop(self, "floatValue", text=text)

    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)
        
    # Custom functions
    def reset(self):
        self.floatValue = 0.0
        self.isDeg = False
        if not self.is_output and len(self.links) != 0:
            self.id_data.links.remove(self.links[0])