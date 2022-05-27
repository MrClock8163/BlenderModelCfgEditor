import bpy
from bpy.types import Node
from . import n_tree

class MCFG_N_BoneList(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "bone"
    
    # Node properties
    def updateBoneCount(self,context):
        numberOfInputs = len(self.inputs)
        countDifference = self.boneCount - numberOfInputs
        
        if countDifference < 0:
            for i in range(numberOfInputs-1,numberOfInputs-1 - abs(countDifference),-1):
                self.inputs.remove(self.inputs[i])
        else:
            for i in range(0,countDifference):
                self.inputs.new('MCFG_S_SkeletonBone',"Bone")
                self.inputs[len(self.inputs)-1].hide_value = True
    
    boneCount: bpy.props.IntProperty(
        name = "Bone count",
        min = 1,
        max = 200,
        default = 1,
        update = updateBoneCount
    )
    
    # Standard functions
    def draw_label(self):
        return "Bone list"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_SkeletonBone', "Bone")
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

    def draw_buttons(self, context, layout):
        layout.prop(self, "boneCount")
        
    # Custom functions
    def process(self):
        boneList = []
        
        for socket in self.inputs:
            if len(socket.links) != 0:
                boneList.append(socket.links[0].from_node.process())
        
        return boneList