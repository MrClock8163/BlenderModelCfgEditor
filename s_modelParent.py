import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelParent(NodeSocket):
    # Description string
    '''Model socket'''
    
    # Mandatory variables
    bl_label = "Input parent"
        
    # Custom variables
    compatibleSockets = []
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0, 0.792, 0.792, 1.0)