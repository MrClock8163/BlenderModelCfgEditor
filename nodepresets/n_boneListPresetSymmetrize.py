import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets
from .. import utility_data as Data

class MCFG_N_BoneListPresetSymmetrize(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - symmetrize"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-symmetrize"
    
    # Node properties
    stringLeft: bpy.props.StringProperty(
        default="left",
        name="Left",
        description = "Indentifier to add to left side bones"
    )
    stringRight: bpy.props.StringProperty(
        default = "right",
        name = "Right",
        description = "Indentifier to add to right side bones"
    )
    
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
    
    # Standard functions
    def draw_label(self):
        return "Bone preset"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_SkeletonBoneList', "Base bone list")
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: symmetrize")
        box.prop(self, "stringLeft")
        box.prop(self, "stringRight")
        
    # Custom functions
    def getBoneList(self):
        if len(self.inputs[0].links) == 0:
            return []
            
        boneList = self.inputs[0].links[0].from_node.process()
        
        if len(boneList) != 0 and (type(boneList[0]) != Data.Bone):
            return []
        
        return boneList
        
    def process(self):
        return Presets.BoneSymmetrize(self.getBoneList(),self.stringLeft,self.stringRight)
        
    def inspect(self):
        for bone in self.process():
            print(bone)