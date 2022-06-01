import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data
from .. import utility_presets as Presets

class MCFG_N_BoneListPresetHouse(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - house standards"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-house-standards"
    
    # Node properties
    damCount: bpy.props.IntProperty(
        name = "Damage",
        description = "Number of damage selections",
        default = 0,
        min = 0,
        max = 100,
        soft_max = 5
    )
    doorCount: bpy.props.IntProperty(
        name = "Doors",
        description = "Number of doors",
        default = 0,
        min = 0,
        max = 100,
        soft_max = 5
    )
    doorHandle: bpy.props.BoolProperty(
        name = "Handles",
        description = "Doors have animated handles",
        default = True
    )
    glassCount: bpy.props.IntProperty(
        name = "Glasses",
        description = "Number of breakable glasses",
        default = 0,
        min = 0,
        max = 100,
        soft_max = 10
    )
    
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
        box.label(text="Name: house standards")
        box.prop(self, "damCount")
        box.prop(self, "doorCount")
        if self.doorCount > 0:
            box.prop(self, "doorHandle")
        box.prop(self, "glassCount")
        
    # Custom functions        
    def process(self):
        return Presets.BoneStandardHouse(self.damCount,self.doorCount,self.doorHandle,self.glassCount)
        
    def inspect(self):
        for bone in self.process():
            print(bone)