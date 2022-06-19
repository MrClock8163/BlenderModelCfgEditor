import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationListPresetGlasses(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - hide glasses"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-list:-hide-glasses"
    
    # Node properties
    glassCount: bpy.props.IntProperty(
        name = "Glasses",
        description = "Nummber glasses to be animated",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 10
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
        box.label(text="Name: hide glasses")
        box.prop(self, "glassCount")
        
    # Custom functions    
    def process(self):
        return Presets.GlassHide(self.glassCount)
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())