import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data

class MCFG_N_Demostrative(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Socket demostrative node'''
    
    # Mandatory variables
    bl_label = "Socket demostrative"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "operator"
    export_type = ""
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Socket-demostrative"
    
    # Standard functions
    def update(self):
        if len(self.inputs) == 0:
            return
            
        self.unlinkInvalidSockets()
    
    # Standard functions
    def draw_label(self):
        return "Socket demostrative"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_SkeletonParent', "Skeleton")
        self.inputs.new('MCFG_S_SkeletonBone', "Bone")
        self.inputs.new('MCFG_S_SkeletonBoneList', "Bone list")
        self.inputs.new('MCFG_S_ModelParent', "Model")
        self.inputs.new('MCFG_S_ModelSection', "Section")
        self.inputs.new('MCFG_S_ModelSectionList', "Section list")
        self.inputs.new('MCFG_S_ModelAnimation', "Animation")
        self.inputs.new('MCFG_S_ModelAnimationList', "Animation list")
        self.inputs.new('MCFG_S_ModelSourceAddress', "Source address")
        self.inputs.new('MCFG_S_List', "List")
        self.inputs.new('MCFG_S_ValueBool', "Boolean")
        self.inputs.new('MCFG_S_ValueFloat', "Float")
        self.inputs.new('MCFG_S_ValueString', "String")
        self.inputs.new('MCFG_S_Universal', "Universal")

    def draw_buttons(self, context, layout): # Node properties
        pass