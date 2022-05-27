import bpy
from bpy.types import NodeSocket

class MCFG_S_ValueFloat(NodeSocket):
    # Description string
    '''Float socket'''
    
    # Mandatory variables
    bl_label = "Input bone"
    
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
    
    # Standard functions
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "floatValue", text=text)

    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)
        
    # Custom functions
    def reset(self):
        self.floatValue = 0.0
        if not self.is_output and len(self.links) != 0:
            self.id_data.links.remove(self.links[0])