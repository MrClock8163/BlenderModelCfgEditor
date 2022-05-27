import bpy
from bpy.types import NodeSocket

class MCFG_S_SkeletonParent(NodeSocket):
    '''Model cfg skeleton parent input socket'''
    
    bl_label = "Input parent"
    
    compatibleSockets = []
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
        
        # for link in self.links:
            # print(self.type)
            # if link.to_socket.bl_idname != self.bl_idname:
                
                # link.is_valid = False
                # link.is_muted = True

    # Socket color
    def draw_color(self, context, node):
        return (0.792, 0.322, 0.067, 1.0)