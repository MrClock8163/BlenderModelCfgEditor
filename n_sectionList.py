import bpy
from bpy.types import Node
from . import n_tree

class MCFG_N_SectionList(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Section list node'''
    
    # Mandatory variables
    bl_label = "Section list"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "model"
    
    # Node properties
    def updateSectionCount(self,context):
        numberOfInputs = len(self.inputs)
        countDifference = self.sectionCount - numberOfInputs
        if countDifference < 0:
            for i in range(numberOfInputs-1,numberOfInputs-1 - abs(countDifference),-1):
                self.inputs.remove(self.inputs[i])
        else:
            for i in range(0,countDifference):
                self.inputs.new('MCFG_S_ModelSection',"Section")
    
    sectionCount: bpy.props.IntProperty(
        name = "Section count",
        min = 1,
        max = 50,
        default = 1,
        update = updateSectionCount
    )
    
    # Standard functions
    def draw_label(self):
        return "Section list"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelSection', "Section")
        self.outputs.new('MCFG_S_ModelSectionList', "Section list")

    def draw_buttons(self, context, layout):
        layout.prop(self, "sectionCount")
        
    # Custom functions
    def process(self):
        sectionList = []
        
        for socket in self.inputs:
            newSection = ""
            if len(socket.links) != 0:
                newSection = socket.links[0].from_node.process()
            else:
                newSection = socket.stringValue.strip()
                
                
            if newSection != "":
                sectionList.append(newSection)
        
        return sectionList