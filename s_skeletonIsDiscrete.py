import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonIsDiscrete(NodeSocket):
    # Description string
    '''Model cfg skeleton isDiscrete input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Input isDiscrete"

    compatibleSockets = []

        
    InputIsDiscretProperty: bpy.props.BoolProperty(
        name="Discrete",
        description="Description",
        default=True
    )
    
    def getValue(self):
        return self.InputIsDiscretProperty
        
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "InputIsDiscretProperty", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1, 1, 0, 1.0)