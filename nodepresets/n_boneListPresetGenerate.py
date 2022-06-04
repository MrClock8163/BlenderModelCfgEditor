import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data
from .. import utility_presets as Presets

class MCFG_N_BoneListPresetGenerate(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - generator"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-generator"
    
    # Node properties
    selectionName: bpy.props.StringProperty(
        default="bone_%",
        name="Bone name",
        description = "Base bone name for the generation\nMark the place for the generated index with a '%'"
    )
    idlength: bpy.props.IntProperty(
        default=2,
        name = "ID length",
        description = "Length of the ID section of the generated bones\nWhere the ID number is fewer digits than this value, leading zeros are introduced\nWhen the value is lower than the digit count of the largest generated ID, that value is applied",
        min = 1,
        max = 50,
        soft_max = 5
    )
    range1: bpy.props.IntProperty(
        default = 1,
        name = "Range start",
        description = "Starting number of generation",
        min = 0,
        max = 1000,
        soft_max = 100
    )
    range2: bpy.props.IntProperty(
        default = 10,
        name = "Range end",
        description = "Ending number of generation",
        min = 1,
        max = 1000,
        soft_max = 100
    )
    baseBone: bpy.props.EnumProperty(
        name = "Base bone",
        description = "Option to set whether a base bone should be created if so, the base bone will be parented as specified and all subsequent bones will be parented to the base",
        default = 'YES',
        items = (
            ('YES',"Generate","Generate base bone"),
            ('NO',"Don't generate","Don't generate base bone")
            
        )
    )
    
    # Standard functions
    def draw_label(self):
        return "Bone preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.inputs.new('MCFG_S_ValueString', "Bone parent")
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: bone generator")
        box.prop(self, "selectionName")
        box.prop(self, "baseBone")
        box.prop(self, "idlength")
        box.prop(self, "range1")
        box.prop(self, "range2")
        
    # Custom functions
    def getSelection(self):        
        return self.selectionName.strip()
    
    def getParent(self):
    
        if len(self.inputs[0].links) == 0:
            return self.inputs[0].stringValue.strip()
            
        parent = self.inputs[0].links[0].from_node.process()
        
        if isinstance(parent,Data.Bone):
            parent = parent.name
        
        return parent
        
    def getAnimName(self):
        return (self.getSelection() + "_rot")
    
    def getMuzzleIndex(self):
        if self.animScope == 'ALL':
            return -1
        else:
            return self.muzzleIndex - 1
        
    def process(self):
        return Presets.BoneGenerator(self.getSelection(),self.getParent(),self.baseBone,self.idlength,[self.range1,self.range2])
        
    def inspect(self):
        for bone in self.process():
            print(bone)
            
    def presetsettings(self):
        settings = []
        
        if self.baseBone != 'YES':
            settings.append(["baseBone",self.baseBone])
            
        return settings