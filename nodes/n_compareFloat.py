import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_CompareFloat(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Float compare node'''
    
    # Mandatory variables
    bl_label = "Float compare"
    bl_icon = 'NONE'
    
    # Custom variables
    node_group = "operator"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Float-compare"
    
    # Node properties
    comparison: bpy.props.EnumProperty(
        name = "Comparison",
        description = "Comparison to perform on the two input values",
        default = 'EQUAL',
        items = (
            ('EQUAL',"A = B",""),
            ('NOTEQUAL',"A != B",""),
            ('GREATER',"A > B",""),
            ('GREATEREQUAL',"A >= B",""),
            ('LESS',"A < B",""),
            ('LESSEQUAL',"A <= B","")
        )
    )
    
    # Standard functions
    def draw_label(self):
        return "Compare"
        
    def init(self, context):
        self.customColor()
        self.inputs.new('MCFG_S_ValueFloat', "A")
        self.inputs.new('MCFG_S_ValueFloat', "B")
        self.outputs.new('MCFG_S_ValueBool', "Value")

    def draw_buttons(self, context, layout):
        layout.prop(self, "comparison",text="")
        
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
        if self.comparison == 'EQUAL':
            return (self.getValueA() == self.getValueB())
        elif self.comparison == 'NOTEQUAL':
            return (self.getValueA() != self.getValueB())
        elif self.comparison == 'GREATER':
            return (self.getValueA() > self.getValueB())
        elif self.comparison == 'GREATEREQUAL':
            return (self.getValueA() >= self.getValueB())
        elif self.comparison == 'LESS':
            return (self.getValueA() < self.getValueB())
        elif self.comparison == 'LESSEQUAL':
            return (self.getValueA() <= self.getValueB())
        
    def inspect(self):
        print(self.process())
        
    def presetsettings(self):
        settings = []
        if self.comparison != 'EQUAL':
            settings.append(["comparison",self.comparison])
        return settings