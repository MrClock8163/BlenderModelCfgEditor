import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data
from .. import utility_presets as Presets

class MCFG_N_BoneListPresetTank(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - tank wheels"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-tank-wheels"
    
    # Node properties
    wheelFixed: bpy.props.IntProperty(
        name = "Fixed",
        description = "Number of not suspended wheels",
        default = 2,
        min = 0,
        max = 100,
        soft_max = 5
    )
    wheelDamping: bpy.props.IntProperty(
        name = "Suspended",
        description = "Number of suspended wheels",
        default = 5,
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
        box.label(text="Name: tank wheels")
        box.prop(self, "wheelFixed")
        box.prop(self, "wheelDamping")
        
    # Custom functions        
    def process(self):
        return Presets.BoneStandardTank(self.wheelFixed,self.wheelDamping)
        
    def inspect(self):
        for bone in self.process():
            print(bone)