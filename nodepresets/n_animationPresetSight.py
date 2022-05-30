import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationPresetSightHide(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - hide sight"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "hide"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-class:-hide-sight"
    
    # Node properties
    selectionName: bpy.props.StringProperty(
        default="sight",
        name="Selection",
        description = "Name of the selection to animate"
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
        box.label(text="Name: sight hide")
        box.prop(self, "selectionName")
        
    # Custom functions
    def getSelection(self):        
        return self.selectionName.strip()
        
    def getAnimName(self):
        return (self.getSelection() + "_hide")
        
    def process(self):
        return Presets.SightHide(self.getAnimName(),self.getSelection())
        
    def inspect(self):
        data = self.process()
        print(data.Print())