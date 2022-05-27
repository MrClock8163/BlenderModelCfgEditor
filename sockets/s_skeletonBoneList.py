import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonBoneList(NodeSocket):
    # Description string
    '''Bone list socket'''
    
    # Mandatory variables
    bl_label = "Input bone list"
    
    # Custom variables
    compatibleSockets = ["MCFG_S_List"]
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (1, 0.1, 0.067, 1.0)