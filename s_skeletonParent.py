import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonParent(NodeSocket):
    # Description string
    '''Skeleton socket'''
    
    # Mandatory variables
    bl_label = "Input parent"
    
    # Custom variables
    compatibleSockets = []
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0.792, 0.322, 0.067, 1.0)