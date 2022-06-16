import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data
from .. import utility_presets as Presets

class MCFG_N_BoneListPresetCar(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - car wheels"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-car-wheels"
    
    # Node properties
    wheels: bpy.props.IntProperty(
        name = "Wheels",
        description = "Number of wheels on one side of the vehicle",
        default = 2,
        min = 2,
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
        box.label(text="Name: car wheels")
        box.prop(self, "wheels")
        
    # Custom functions        
    def process(self):
        return Presets.BoneStandardCar(self.wheels)
        
    def inspect(self):
        for bone in self.process():
            print(bone)