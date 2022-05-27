import bpy
from bpy.types import NodeSocket

class MCFG_S_List(NodeSocket):
    # Description string
    '''Model cfg skeleton bones input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "List"
    
    compatibleSockets = ["MCFG_S_SkeletonBoneList","MCFG_S_ModelSectionList","MCFG_S_ModelAnimationList"]
    
    
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)