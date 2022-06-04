import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationListPresetBulletsHide(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - hide bullets"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "hide"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-list:-hide-bullets"
    
    # Node properties
    selectionName: bpy.props.StringProperty(
        default="bullet_%",
        name="Selection name",
        description = "Name of the selection to animate\nMark the place for the generated index with a '%'"
    )
    animScope: bpy.props.EnumProperty(
        name = "Scope",
        description = "Whether the animation should affect a certain muzzle or any",
        default = 'ALL',
        items = (
            ('ALL',"Not muzzle specific","Animation affects any muzzles"),
            ('SPECIFIC',"Muzzle specific","Animation affects a specific muzzle")
        )
    )
    muzzleIndex: bpy.props.IntProperty(
        name = "Muzzle index",
        description = "Index of the muzzle to affect",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 5
    )
    idlength: bpy.props.IntProperty(
        default=2,
        name = "ID length",
        description = "Length of the ID section of the generated bones\nWhere the ID number is fewer digits than this value, leading zeros are introduced\nWhen the value is lower than the digit count of the largest generated ID, that value is applied",
        min = 1,
        max = 50,
        soft_max = 5
    )
    magCapacity: bpy.props.IntProperty(
        name = "Magazine capacity",
        description = "Ammo capacity of the magazine",
        default = 20,
        min = 1,
        max = 1000,
        soft_max = 200
    )
    interval1: bpy.props.IntProperty(
        name = "First bullet",
        description = "Index of first bullet to be animated",
        default = 1,
        min = 1,
        max = 100
    )
    interval2: bpy.props.IntProperty(
        name = "Last bullet",
        description = "Index of last bullet to be animated",
        default = 1,
        min = 1,
        max = 100
    )
    
    # Standard functions
    def draw_label(self):
        return "Hide preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ModelAnimationList', "Animation list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: bullet hide")
        box.prop(self, "selectionName")
        box.prop(self, "animScope")
        if self.animScope == 'SPECIFIC':
            box.prop(self, "muzzleIndex")
        box.prop(self, "idlength")
        box.prop(self, "magCapacity")
        box.prop(self, "interval1")
        box.prop(self, "interval2")
        
    # Custom functions
    def getSelection(self):        
        return self.selectionName.strip()
        
    def getAnimName(self):
        return (self.getSelection() + "_rot")
    
    def getMuzzleIndex(self):
        if self.animScope == 'ALL':
            return -1
        else:
            return self.muzzleIndex - 1
        
    def process(self):
        return Presets.BulletHide(self.getSelection(),self.getMuzzleIndex(),self.idlength,self.magCapacity,[self.interval1,self.interval2])
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())
            
    def presetsettings(self):
        settings = []
        if self.animScope != 'ALL':
            settings.append(["animScope",self.animScope])
        return settings