import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_MathBasic(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Basic math node'''
    
    # Mandatory variables
    bl_label = "Basic math"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "operator"
    
    # Node properties
    operation: bpy.props.EnumProperty (
        name = "",
        description = "Type of operation to perform",
        default = 'ADD',
        items = (
            ('ADD',"A + B","Perform addition"),
            ('SUBS',"A - B","Perform substraction"),
            ('MULTIPLY',"A x B","Perform multiplication"),
            ('DIVIDE',"A / B","Perform division")
        )
    )
    
    # Standard functions
    def draw_label(self):
        return "Basic math"
        
    def init(self, context):
        self.customColor()
        self.inputs.new('MCFG_S_ValueFloat', "A")
        self.inputs.new('MCFG_S_ValueFloat', "B")
        self.outputs.new('MCFG_S_ValueFloat', "Result")

    def draw_buttons(self, context, layout):
        layout.prop(self, "operation")
        
    # Custom functions
    def getValueA(self):
        if len(self.inputs[0].links) == 0:
            return round(self.inputs[0].floatValue,6)
            
        return self.inputs[0].links[0].from_node.process()
        
    def getValueB(self):
        if len(self.inputs[1].links) == 0:
            return round(self.inputs[1].floatValue,6)
            
        return self.inputs[1].links[0].from_node.process()
    
    def process(self):
        if self.operation == 'ADD':
            return self.getValueA() + self.getValueB()
        elif self.operation == 'SUBS':
            return self.getValueA() - self.getValueB()
        elif self.operation == 'MULTIPLY':
            return self.getValueA() * self.getValueB()
        elif self.operation == 'DIVIDE':
            if self.getValueB() == 0:
                return 0
            return self.getValueA() / self.getValueB()
            
    def inspect(self):
        print(self.process())