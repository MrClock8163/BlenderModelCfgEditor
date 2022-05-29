import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_JoinList(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Join lists node'''
    
    # Mandatory variables
    bl_label = "Join lists"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "operator"
    
    # Node properties
    def updateListCount(self,context):
        numberOfInputs = len(self.inputs)
        countDifference = self.listCount - numberOfInputs
        
        if countDifference < 0:
            for i in range(numberOfInputs-1,numberOfInputs-1 - abs(countDifference),-1):
                self.inputs.remove(self.inputs[i])
        else:
            for i in range(0,countDifference):
                self.inputs.new('MCFG_S_List',"List")
                self.inputs[len(self.inputs)-1].hide_value = True
    
    listCount: bpy.props.IntProperty(
        name = "List count",
        min = 1,
        max = 200,
        default = 1,
        update = updateListCount
    )
    
    # Standard functions
    def draw_label(self):
        return "Join lists"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_List', "List")
        self.outputs.new('MCFG_S_List', "Output list")

    def draw_buttons(self, context, layout):
        layout.prop(self, "listCount")
        
    # Custom functions
    def process(self):
        joinedList = []
        
        for socket in self.inputs:
            if len(socket.links) != 0:
                joinedList += (socket.links[0].from_node.process())
                
        if len(joinedList) == 0:
            return []
            
        # only return items if they are of same type
        for item in joinedList:
            if not isinstance(item,type(joinedList[0])):
                return []
        
        return joinedList
        
    def inspect(self):
        print("Join list nodes cannot be inspected due to the uncertain nature of their returned data")