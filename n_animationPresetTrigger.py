import bpy
from bpy.types import Node
from . import n_tree
from . import utility_presets as Presets

class MCFG_N_AnimationPresetTriggerRot(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - rotate trigger"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "rotation"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    selectionName: bpy.props.StringProperty(
        default="trigger",
        name="Selection",
        description = "Name of the selection to animate"
    )
    axisName: bpy.props.StringProperty(
        default="trigger_axis",
        name="Axis",
        description = "Name of the rotation axis"
    )
    rotationLimit: bpy.props.IntProperty(
        default = -30,
        name = "Angle",
        description = "Angle of the rotation of the trigger in degrees",
        min = -90,
        max = 90,
        soft_min = -30,
        soft_max = 30
    )
    
    # Standard functions
    def draw_label(self):
        return "Rotation preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: trigger rotation")
        box.prop(self, "selectionName")
        box.prop(self, "axisName")
        box.prop(self, "rotationLimit")
        
    # Custom functions
    def getSelection(self):        
        return self.selectionName.strip()
        
    def getAnimName(self):
        return (self.getSelection() + "_rot")
        
    def getAxis(self):
        return self.axisName.strip()
        
    def getAngle(self):
        return (self.rotationLimit * (3.141592653589793/180))
        
    def process(self):
        return Presets.TriggerRot(self.getAnimName(),self.getSelection(),self.getAxis(),self.getAngle())

class MCFG_N_AnimationPresetTriggerMove(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - move trigger"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "translation"
    animation_type_min_value = "Offset0"
    animation_type_max_value = "Offset1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    selectionName: bpy.props.StringProperty(
        default="trigger",
        name="Selection",
        description = "Name of the selection to animate"
    )
    axisName: bpy.props.StringProperty(
        default="trigger_axis",
        name="Axis",
        description = "Name of the rotation axis"
    )
    translationLimit: bpy.props.IntProperty(
        default = 1,
        name = "Offset",
        description = "Offset coefficient relative to the length of the defined axis",
        min = -100,
        max = 100,
        soft_min = -5,
        soft_max = 5
    )
    
    # Standard functions
    def draw_label(self):
        return "Translation preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: trigger translation")
        box.prop(self, "selectionName")
        box.prop(self, "axisName")
        box.prop(self, "translationLimit")
        
    # Custom functions
    def getSelection(self):        
        return self.selectionName.strip()
        
    def getAnimName(self):
        return (self.getSelection() + "_move")
        
    def getAxis(self):
        return self.axisName.strip()
        
    def getOffset(self):
        return (self.translationLimit)
        
    def process(self):
        return Presets.TriggerMove(self.getAnimName(),self.getSelection(),self.getAxis(),self.getOffset())