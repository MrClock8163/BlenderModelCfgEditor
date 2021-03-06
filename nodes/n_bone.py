import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data

class MCFG_N_Bone(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone item node'''
    
    # Mandatory variables
    bl_label = "Bone item"
    bl_icon = 'BONE_DATA'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-item"
    
    # Node properties
    def updateBoneName(self,context):
        self.name = "Bone: {}".format(self.boneName)
        
    boneName: bpy.props.StringProperty(
        default="Bone",
        name="Name",
        description = "Name of the bone",
        update = updateBoneName
    )
    
    # Standard functions
    def draw_label(self):
        return "Bone"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_SkeletonBone', "Parent")
        self.inputs[0].hide_value = True
        self.outputs.new('MCFG_S_SkeletonBone', "Bone")

    def draw_buttons(self, context, layout):
        layout.prop(self, "boneName")
        
    # Custom functions
    def getBoneName(self):
        return self.boneName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getBoneName()

    def process(self):
        newBone = Data.Bone(self.getBoneName(),self.getParentName())
        
        return newBone
        
    def inspect(self):
        print(self.process())