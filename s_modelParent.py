import bpy
from bpy.types import NodeSocket

class MCFG_S_ModelParent(NodeSocket):
    '''Model cfg model parent input socket'''
    
    compatibleSockets = []
    
    bl_label = "Input parent"
    def draw(self, context, layout, node, text):
        layout.label(text=text)
        
        # for link in self.links:
            # print(self.type)
            # if link.to_socket.bl_idname != self.bl_idname:
                
                # link.is_valid = False
                # link.is_muted = True

    # Socket color
    def draw_color(self, context, node):
        return (0, 0.792, 0.792, 1.0)