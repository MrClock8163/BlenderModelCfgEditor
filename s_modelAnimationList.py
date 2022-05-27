import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelAnimationList(NodeSocket):
    # Description string
    '''Animation list socket'''
    
    # Mandatory variables
    bl_label = "Input animation list"
    
    # Custom variables
    compatibleSockets = ["MCFG_S_List"]
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0, 0.1, 0.9, 1.0)