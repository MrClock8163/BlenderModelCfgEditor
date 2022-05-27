import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelAnimation(NodeSocket):
    # Description string
    '''Animation socket'''
    
    # Mandatory variables
    bl_label = "Input animation"
    
    # Custom variables
    compatibleSockets = []
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0, 0.1, 0.9, 1.0)
        
    # Custom functions
    def GetValue(self):
        if self.is_output:
            return self.links[0].from_node.Process()
        else:
            return None