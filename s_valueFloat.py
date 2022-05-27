import bpy
from bpy.types import NodeSocket

class MCFG_S_ValueFloat(NodeSocket):
    # Description string
    '''Model cfg skeleton bones input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Input bone"
    
    
    compatibleSockets = []
    
    floatValue: bpy.props.FloatProperty(
        name = "Value",
        default = 0.0,
        min = -1000,
        max = 1000,
        soft_max = 100,
        soft_min = -100
    )
    
    def reset(self):
        self.floatValue = 0.0
        if not self.is_output and len(self.links) != 0:
            self.id_data.links.remove(self.links[0])
    
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "floatValue", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)