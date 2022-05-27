import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelAnimation(NodeSocket):
    # Description string
    '''Model cfg animation input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Input animation"

    compatibleSockets = []
    
    def GetValue(self):
        if self.is_output:
            return self.links[0].from_node.Process()
        else:
            return None
                
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (0, 0.1, 0.9, 1.0)