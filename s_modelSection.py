import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelSection(NodeSocket):
    # Description string
    '''Model cfg model section input'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Input section"

    stringValue: bpy.props.StringProperty(
        name = "Name",
        default = ""
    )
                
    def GetValue(self):
        return self.stringValue.strip()
        
    compatibleSockets = []
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "stringValue", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (0, 0.8, 0.1, 1.0)