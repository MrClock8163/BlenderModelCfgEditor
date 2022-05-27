import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonBone(NodeSocket):
    # Description string
    '''Model cfg skeleton bones input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Input bone"
    
    compatibleSockets = []
    
    boneName: bpy.props.StringProperty(
        name = "Name",
        default = "Bone",
        description = "Name of the bone item"
    )
                
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)
        return
        
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "boneName", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1, 0.1, 0.067, 1.0)