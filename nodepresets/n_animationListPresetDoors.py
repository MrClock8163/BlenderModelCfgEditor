import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationListPresetDoorsRot(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - rotate doors"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/None:-Animation-list:-rotate-doors"
    
    # Node properties
    doorFirst: bpy.props.IntProperty(
        name = "First",
        description = "First door to be animated",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 5
    )
    doorLast: bpy.props.IntProperty(
        name = "Last",
        description = "Last door to be animated",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 5
    )
    doorHandle: bpy.props.BoolProperty(
        name = "Handles",
        description = "Doors have animated handles",
        default = True
    )
    angleDoor: bpy.props.IntProperty(
        name = "Door angle",
        description = "Door rotation angle",
        default = 100,
        min = -180,
        max = 180
    )
    angleHandle: bpy.props.IntProperty(
        name = "Handle angle",
        description = "Door handle rotation angle",
        default = 30,
        min = -180,
        max = 180
    )
    
    # Standard functions
    def draw_label(self):
        return "Rotation preset"
        
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ModelAnimationList', "Animation list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: rotate doors")
        box.prop(self, "doorFirst")
        box.prop(self, "doorLast")
        box.prop(self, "doorHandle")
        box.prop(self, "angleDoor")
        if self.doorHandle:
            box.prop(self, "angleHandle")
        
    # Custom functions
    def rad(angle):
        return (angle * (3.141592653589793/180))
    
    def getRange(self):
        doorRange = [self.doorFirst,self.doorLast]
        doorRange.sort()
        return doorRange
    
    def process(self):
        return Presets.DoorRot(self.getRange(),self.doorHandle,self.angleDoor * (3.141592653589793/180),self.angleHandle * (3.141592653589793/180))
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())
            
class MCFG_N_AnimationListPresetDoorsMove(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - move doors"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "translation"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-list:-move-doors"
    
    # Node properties
    doorFirst: bpy.props.IntProperty(
        name = "First",
        description = "First door to be animated",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 5
    )
    doorLast: bpy.props.IntProperty(
        name = "Last",
        description = "Last door to be animated",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 5
    )
    offsetDoor: bpy.props.IntProperty(
        name = "Door offset",
        description = "Door translation offset",
        default = 1,
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
        self.outputs.new('MCFG_S_ModelAnimationList', "Animation list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: move doors")
        box.prop(self, "doorFirst")
        box.prop(self, "doorLast")
        box.prop(self, "offsetDoor")
        
    # Custom functions    
    def getRange(self):
        doorRange = [self.doorFirst,self.doorLast]
        doorRange.sort()
        return doorRange
    
    def process(self):
        return Presets.DoorMove(self.getRange(),self.offsetDoor)
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())