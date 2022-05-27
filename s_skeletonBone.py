import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonBone(NodeSocket):
    # Description string
    '''Bone socket'''
    
    # Mandatory variables
    bl_label = "Input bone"
    
    # Custom variables
    compatibleSockets = []
    
    # Socket properties
    boneName: bpy.props.StringProperty(
        name = "Name",
        default = "Bone",
        description = "Name of the bone item"
    )
    
    # Standard functions
    def draw(self, context, layout, node, text):
        layout.label(text=text)
        return
        
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "boneName", text=text)

    def draw_color(self, context, node):
        return (1, 0.1, 0.067, 1.0)