import bpy
from bpy.types import Node
from . import n_tree
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_BoneListPresetStandardWeapon(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Bone list nod'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Bone list - weapon standards"
    # Icon identifier
    bl_icon = 'ANIM'
    
    node_group = "bone"
    
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        # layout.label(text="Node settings")
        box = layout.box()
        box.label(text="Name: weapon standards")

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.label(text="Name: weapon standards")
        
    def process(self):
        return Presets.BoneStandardWeapon()

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Bone preset"