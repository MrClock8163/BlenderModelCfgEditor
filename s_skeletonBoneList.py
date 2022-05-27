import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonBoneList(NodeSocket):
    # Description string
    '''Model cfg skeleton bones input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Input bone list"

    compatibleSockets = ["MCFG_S_List"]
                
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1, 0.1, 0.067, 1.0)