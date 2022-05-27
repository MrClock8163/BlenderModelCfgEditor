import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelSectionList(NodeSocket):
    # Description string
    '''Section list socket'''
    
    # Mandatory variables
    bl_label = "Input section list"
    
    # Custom variables
    compatibleSockets = ["MCFG_S_List"]
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0, 0.8, 0.1, 1.0)