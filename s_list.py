import bpy
from bpy.types import NodeSocket

class MCFG_S_List(NodeSocket):
    # Description string
    '''Generic list socket'''
    
    # Mandatory variables
    bl_label = "List"
    
    # Custom variables
    compatibleSockets = ["MCFG_S_SkeletonBoneList","MCFG_S_ModelSectionList","MCFG_S_ModelAnimationList"]
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)