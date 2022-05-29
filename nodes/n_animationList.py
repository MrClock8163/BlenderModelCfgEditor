import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_AnimationList(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animations list node'''
    
    # Mandatory variables
    bl_label = "Animation list"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "animation"
    
    # Node properties
    def updateAnimCount(self,context):
        numberOfInputs = len(self.inputs)
        countDifference = self.animCount - numberOfInputs
        if countDifference < 0:
            for i in range(numberOfInputs-1,numberOfInputs-1 - abs(countDifference),-1):
                self.inputs.remove(self.inputs[i])
        else:
            for i in range(0,countDifference):
                self.inputs.new('MCFG_S_ModelAnimation',"Animation")
    
    animCount: bpy.props.IntProperty(
        name = "Animation count",
        min = 1,
        max = 200,
        default = 1,
        update = updateAnimCount
    )
    
    # Standard functions
    def draw_label(self):
        return "Animation list"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Animation")
        self.outputs.new('MCFG_S_ModelAnimationList', "Animation list")

    def draw_buttons(self, context, layout):
        layout.prop(self, "animCount")

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def process(self):
        animList = []
        
        for socket in self.inputs:
            if len(socket.links) != 0:
                animList.append(socket.links[0].from_node.process())
                
        return animList
    
    def inspect(self):
        data = self.process()
        
        for anim in data:
            print(anim.Print())