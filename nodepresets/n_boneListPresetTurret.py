import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data
from .. import utility_presets as Presets

class MCFG_N_BoneListPresetTurret(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - turrets"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-turrets"
    
    # Node properties
    turretCount: bpy.props.IntProperty(
        name = "Turrets",
        description = "Number of turrets",
        default = 1,
        min = 0,
        max = 100,
        soft_max = 5
    )
    hasCommander: bpy.props.BoolProperty(
        name = "Commander",
        description = "Should a commander view bone be generated?",
        default = False
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
        box.label(text="Name: turrets")
        box.prop(self, "turretCount")
        box.prop(self, "hasCommander")
        
    # Custom functions        
    def process(self):
        return Presets.BoneStandardTurret(self.turretCount,self.hasCommander)
        
    def inspect(self):
        for bone in self.process():
            print(bone)