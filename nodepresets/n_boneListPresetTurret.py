import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data
from .. import utility_presets as Presets

class MCFG_N_BoneListPresetTurret(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - turret"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-turret"
    
    # Node properties
    identifier: bpy.props.StringProperty(
        name = "ID",
        description = "Identifier of the turret (the value will be inserted into the generated bone names)",
        default = "main"
    )
    
    # Standard functions
    def draw_label(self):
        return "Bone preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.inputs.new('MCFG_S_ValueString', "Parent")
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: turret")
        box.prop(self, "identifier")
        
    # Custom functions
    def getIdentifier(self):
        return self.identifier.strip()
        
    def getParent(self):

        if len(self.inputs[0].links) == 0:
            return self.inputs[0].stringValue.strip()
            
        parent = self.inputs[0].links[0].from_node.process()
        
        if isinstance(parent,Data.Bone):
            parent = parent.name
    
        return parent
        
    def process(self):
        return Presets.BoneStandardTurret(self.getIdentifier(),self.getParent())
        
    def inspect(self):
        for bone in self.process():
            print(bone)