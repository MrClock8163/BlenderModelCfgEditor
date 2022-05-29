import bpy
from bpy.types import NodeSocket

class MCFG_S_Universal(NodeSocket):
    # Description string
    '''Universal socket'''
    
    # Mandatory variables
    bl_label = "Universal value"
    
    # Custom variables
    compatibleSockets = []
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (1.0,1.0,1.0,1.0)