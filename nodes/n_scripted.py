import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_Scripted(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Custom scripted node'''
    
    # Mandatory variables
    bl_label = "Custom script"
    bl_icon = 'FILE_SCRIPT'
    
    # Custom variables
    node_group = "operator"
    process_type = "scripted"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Custom-script"
    
    # Node properties
    def updateInputCount(self,context):
        numberOfInputs = len(self.inputs)
        countDifference = self.inputCount - numberOfInputs
        
        if countDifference < 0:
            for i in range(numberOfInputs-1,numberOfInputs-1 - abs(countDifference),-1):
                self.inputs.remove(self.inputs[i])
        else:
            for i in range(0,countDifference):
                self.inputs.new('MCFG_S_Universal',"Input")
                self.inputs[len(self.inputs)-1].hide_value = True
    
    script: bpy.props.PointerProperty(type=bpy.types.Text)
    
    outputData: bpy.props.EnumProperty(
        name = "Output type",
        description = "The script returns a skeleton or model class",
        default = 'UNIV',
        items = (
            ('UNIV',"","Universal data to be linked to other nodes (string, float, bone, animation, etc.)",'LINKED',0),
            ('SKELETON',"","Skeleton class",'ARMATURE_DATA',1),
            ('MODEL',"","Model class",'OBJECT_DATA',2)
        )
    )
    
    inputCount: bpy.props.IntProperty(
        name = "Inputs",
        description = "Number of script inputs",
        default = 0,
        min = 0,
        max = 10,
        update = updateInputCount
    )
    
    # Standard functions
    def draw_label(self):
        return "Custom script"
        
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_Universal', "Output")

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)
        # row.label(text="Script:")
        layout.prop(self, "script",text="Script")
        row = layout.row(align=True)
        row.label(text="Data:")
        row.prop(self, "outputData",expand=True,text="")
        layout.prop(self, "inputCount")
        
    # Custom functions
    def process(self):
        if not self.script:
            return None
        
        returnValue = ""
        globvars = {}
        locvars = {}
        
        for i in range(len(self.inputs)):
            locvars["input_" + str(i)] = ""
            if len(self.inputs[i].links) != 0:
                locvars["input_" + str(i)] = self.inputs[i].links[0].from_node.process()
                locvars["input_node_" + str(i)] = self.inputs[i].links[0].from_node
        
        script = compile(self.script.as_string(),self.script.name,'exec')
        exec(script,globvars,locvars)
        
        if "result" in locvars.keys():
            returnValue = locvars.get("result")
        
        return returnValue
            
    def inspect(self):
        print(self.process())
    
    def presetsettings(self):
        settings = []
        if self.inputCount != 0:
            settings.append(["inputCount",self.inputCount])
        return settings