import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationListPresetTurret(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - turret"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "hide"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-list:-turret"
    
    # Node properties
    identifier: bpy.props.StringProperty(
        name = "ID",
        description = "Identifier of the turret (the value will be inserted into the generated selection and class names)",
        default = "main"
    )
    isMain: bpy.props.BoolProperty(
        name = "Main turret",
        description = "True: the animation source values will be tied to the default 'maingun' and 'mainturret' which do not need to be configured specially in the general vehicle config, False: sources will be generated",
        default = True
    )
    recoilOffset: bpy.props.FloatProperty(
        name = "Recoil offset",
        description = "Offset value for recoil animation (leave 0 if recoil animation is not needed)",
        min = -50,
        max = 50,
        soft_min = 5,
        soft_max = 5,
        default = -1
    )
    
    # Standard functions
    def draw_label(self):
        return "Mixed preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ModelAnimationList', "Animation list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: turret")
        box.prop(self, "identifier")
        box.prop(self, "isMain")
        box.prop(self, "recoilOffset")
        
    # Custom functions
    def getIdentifier(self):
        return self.identifier.strip()
        
    def getOffset(self):
        return round(self.recoilOffset,6)
    
    def process(self):
        return Presets.TurretRot(self.getIdentifier(),self.isMain,self.recoilOffset)
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())