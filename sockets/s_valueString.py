import bpy
from bpy.types import NodeSocket

class MCFG_S_ValueString(NodeSocket):
    # Description string
    '''String socket'''
    
    # Mandatory variables
    bl_label = "String value"
    
    # Custom variables
    compatibleSockets = ["MCFG_S_SkeletonBone"]
    
    # Socket properties
    stringValue: bpy.props.StringProperty(
        name = "Value",
        default = ""
    )
    
    # Standard functions
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "stringValue", text=text)

    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 1.0)
        
    # Custom functions
    def reset(self):
        self.stringValue = ""
        if not self.is_output and len(self.links) != 0:
            self.id_data.links.remove(self.links[0])