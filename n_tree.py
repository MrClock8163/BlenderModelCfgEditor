import bpy
from bpy.types import NodeTree, NodeSocket
import nodeitems_utils
from nodeitems_utils import NodeCategory

# Node editor space
class MCFG_N_Tree(NodeTree):
    # Description string
    '''Arma 3 model config editor'''
    
    # Mandatory variables
    bl_label = "Model Config Editor"
    bl_icon = 'MESH_CUBE'

# Mix-in node base class
class MCFG_N_Base:
    
    # Custom variables
    node_group = "default"
    incompatible_nodes = []
    process_type = ""
    doc_url = ""
    
    def unlinkInvalidSockets(self):
        for socket in self.inputs:
            if len(socket.links) != 0 and not (socket.links[0].from_socket.bl_idname == socket.bl_idname or socket.links[0].from_socket.bl_idname in socket.compatibleSockets or socket.bl_idname == "MCFG_S_Universal" or socket.links[0].from_socket.bl_idname == "MCFG_S_Universal"):
                socket.id_data.links.remove(socket.links[0])
                
            if len(socket.links) != 0 and socket.enabled == False:
                socket.id_data.links.remove(socket.links[0])
                
            if len(socket.links) != 0 and socket.links[0].from_node.bl_idname in socket.node.incompatible_nodes:
                socket.id_data.links.remove(socket.links[0])
                
    def update(self):
        self.unlinkInvalidSockets()
    
    def customColor(self):
        addonPrefs = bpy.context.preferences.addons[__package__].preferences
        if addonPrefs.useCustomColors:
            self.use_custom_color = True
            if self.node_group == "skeleton":
                cColor = addonPrefs.customColorSkeleton
            elif self.node_group == "bone":
                cColor = addonPrefs.customColorBones
            elif self.node_group == "model":
                cColor = addonPrefs.customColorModel
            elif self.node_group == "section":
                cColor = addonPrefs.customColorSection
            elif self.node_group == "animation":
                cColor = addonPrefs.customColorAnimations
            elif self.node_group == "operator":
                cColor = addonPrefs.customColorOperator
            else:
                cColor = (0.2,0.2,0.2)
            self.color = cColor
    
    def presetsettings(self):
        return []
        
    def presetpostsettings(self):
        return []
    
    def process(self):
        print("Process function is not defined for: " + str(self))
        return None
        
    def inspect(self):
        print("Inspect function is not defined for: " + str(self))
        return None

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'

    def copy(self, node):
        pass

    def free(self):
        pass

class MCFG_N_Category(NodeCategory):
    # Standard functions
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'MCFG_N_Tree'