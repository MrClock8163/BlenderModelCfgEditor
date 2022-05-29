import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_BoneListPresetStandardWeapon(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - weapon standards"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    
    # Standard functions
    def draw_label(self):
        return "Bone preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: weapon standards")
        
    # Custom functions
    def process(self):
        return Presets.BoneStandardWeapon()
        
    def inspect(self):
        for bone in self.process():
            print(bone)