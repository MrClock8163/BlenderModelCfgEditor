import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelSection(NodeSocket):
    # Description string
    '''Section socket'''
    
    # Mandatory variables
    bl_label = "Input section"
    
    # Custom variables
    compatibleSockets = []
    
    # Socket properties
    stringValue: bpy.props.StringProperty(
        name = "Name",
        default = ""
    )
    
    # Standard functions
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "stringValue", text=text)

    def draw_color(self, context, node):
        return (0, 0.8, 0.1, 1.0)
        
    # Custom functions
    def GetValue(self):
        return self.stringValue.strip()