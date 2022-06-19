import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_LogicBasic(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Basic logic node'''
    
    # Mandatory variables
    bl_label = "Basic logic"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "operator"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Basic-logic"
    
    # Node properties
    def updateOperation(self,context):
        if len(self.inputs) != 2:
            return
            
        self.inputs[1].enabled = self.operation != 'NOT'
    
    operation: bpy.props.EnumProperty(
        name = "Operation",
        description = "Logical operation",
        default = 'AND',
        update = updateOperation,
        items = (
            ('AND',"A and B",""),
            ('OR',"A or B",""),
            ('NOT',"not A","")
        )
    )
    
    # Standard functions
    def draw_label(self):
        return "Basic logic"
        
    def init(self, context):
        self.customColor()
        self.inputs.new('MCFG_S_ValueBool', "A")
        self.inputs.new('MCFG_S_ValueBool', "B")
        self.outputs.new('MCFG_S_ValueBool', "Value")

    def draw_buttons(self, context, layout):
        layout.prop(self, "operation",text="")
        
    # Custom functions
    def getValueA(self):
        if len(self.inputs[0].links) == 0:
            return self.inputs[0].boolValue
            
        return self.inputs[0].links[0].from_node.process()
        
    def getValueB(self):
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].boolValue
            
        return self.inputs[1].links[0].from_node.process()
        
    def process(self):
        if self.operation == 'AND':
            return (self.getValueA() and self.getValueB())
        elif self.operation == 'OR':
            return (self.getValueA() or self.getValueB())
        elif self.operation == 'NOT':
            return (not self.getValueA())
        
    def inspect(self):
        print(self.process())
        
    def presetsettings(self):
        settings = []
        if self.operation != 'AND':
            settings.append(["operation",self.operation])
        return settings