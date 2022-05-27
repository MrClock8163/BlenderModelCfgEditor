import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelSourceAddress(NodeSocket):
    # Description string
    '''Model cfg skeleton bones input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Source address"
    
    compatibleSockets = []
    
    typeItems = (
        ('CLAMP', "Clamp", "Clamp the animation between the min and max values"),
        ('LOOP', "Loop", "Loop the animation past the min and max values"),
        ('MIRROR', "Mirror", "Mirror the animation past the min and max values")
    )
    
    typeValue: bpy.props.EnumProperty(
        name = "Source address",
        items = typeItems,
        description = "Definition for source interval handling",
        default = 'CLAMP'
    )
                
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "typeValue", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)