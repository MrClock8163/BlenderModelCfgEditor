import bpy
from bpy.types import NodeTree, NodeSocket
import nodeitems_utils
from nodeitems_utils import NodeCategory


# Derived from the NodeTree base type, similar to Menu, Operator, Panel, etc.
class MCFG_N_Tree(NodeTree):
    # Description string
    '''Arma 3 model config editor'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomTreeType'
    # Label for nice name display
    bl_label = "Model config editor"
    # Icon identifier
    bl_icon = 'MESH_CUBE'
    
    
# Mix-in class for all custom nodes in this tree type.
# Defines a poll function to enable instantiation.
class MCFG_N_Base:
    
    node_group = "default"
    incompatible_nodes = []
    export_type = ""
    
    def unlinkInvalidSockets(self):
        for socket in self.inputs:
            # print(socket)
            if len(socket.links) != 0 and not (socket.links[0].from_socket.bl_idname == socket.bl_idname or socket.links[0].from_socket.bl_idname in socket.compatibleSockets):
                # print("Unlinking invalid connection")
                socket.id_data.links.remove(socket.links[0])
            if len(socket.links) != 0 and socket.enabled == False:
                # print("Unlinking hidden socket")
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
            elif self.node_group == "model":
                cColor = addonPrefs.customColorModel
            elif self.node_group == "bone":
                cColor = addonPrefs.customColorBones
            elif self.node_group == "animation":
                cColor = addonPrefs.customColorAnimations
            else:
                cColor = (1.0,1.0,1.0)
            self.color = cColor
            
    def Validate(self):
        return [False,"Validate function is not defined for: " + str(self)]
            
    def Process(self):
        return None
        print("Process function is not defined for: " + str(self))

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
        
        
class MCFG_N_Frame(bpy.types.NodeFrame):
    bl_label = "Frame"

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
        

class MCFG_N_Category(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'MCFG_N_Tree'