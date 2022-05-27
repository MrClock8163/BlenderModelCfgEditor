import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonIsDiscrete(NodeSocket):
    # Description string
    '''IsDiscrete socket'''
    
    # Mandatory variables
    bl_label = "Input isDiscrete"
    
    # Custom variables
    compatibleSockets = []
    
    # Socket properties
    InputIsDiscretProperty: bpy.props.BoolProperty(
        name="Discrete",
        description="Description",
        default=True
    )
    
    # Standard functions
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "InputIsDiscretProperty", text=text)

    def draw_color(self, context, node):
        return (1, 1, 0, 1.0)
        
    # Custom functions
    def getValue(self):
        return self.InputIsDiscretProperty