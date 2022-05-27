import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelSourceAddress(NodeSocket):
    # Description string
    '''Source address socket'''
    
    # Mandatory variables
    bl_label = "Source address"
    
    # Custom variables
    compatibleSockets = []
    
    # Socket properties
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
    
    # Standard functions
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "typeValue", text=text)

    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)