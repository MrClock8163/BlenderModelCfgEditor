import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationPresetMagazineHide(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - hide magazine"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-class:-hide-magazine"
    
    # Node properties
    selectionName: bpy.props.StringProperty(
        default="magazine",
        name="Selection",
        description = "Name of the selection to animate"
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
    
    # Standard functions
    def draw_label(self):
        return "Hide preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: magazine hide")
        box.prop(self, "selectionName")
        box.prop(self, "animScope")
        if self.animScope == 'SPECIFIC':
            box.prop(self, "muzzleIndex")
        
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
        return Presets.MagazineHide(self.getSelection(),self.getMuzzleIndex())
        
    def inspect(self):
        data = self.process()
        print(data.Print())
            
    def presetsettings(self):
        settings = []
        if self.animScope != 'ALL':
            settings.append(["animScope",self.animScope])
        return settings