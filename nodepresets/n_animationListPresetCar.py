import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationListPresetCarWheels(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - car wheels"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-list:-car-wheels"
    
    # Node properties
    wheels: bpy.props.IntProperty(
        name = "Wheels",
        description = "Number of wheels on one side of the vehicle",
        default = 2,
        min = 2,
        max = 100,
        soft_max = 10
    )
    dampMin: bpy.props.FloatProperty(
        name = "Compression",
        description = "Maximal damper compression offset from startion position (absolute value)",
        default = 0.5,
        min = 0,
        max = 100,
        soft_max = 1
    )
    dampMax: bpy.props.FloatProperty(
        name = "Expansion",
        description = "Maximal damper expansion offset from startion position (absolute value)",
        default = 0.5,
        min = 0,
        max = 100,
        soft_max = 1
    )
    damageOffset: bpy.props.FloatProperty(
        name = "Deflation",
        description = "Tire deflation offset for when the tire is damaged, but not destroyed",
        default = 0.2,
        min = 0,
        max = 100,
        soft_max = 1
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
        box.label(text="Name: car wheels")
        box.prop(self, "wheels")
        box.prop(self, "dampMin")
        box.prop(self, "dampMax")
        box.prop(self, "damageOffset")
        
    # Custom functions
    def getDamping(self):
        dampRange = [round(-self.dampMin,6),round(self.dampMax,6)]
        dampRange.sort()
        
        return dampRange
    
    def getDeflation(self):
        return round(self.damageOffset,6)
        
    def process(self):
        return Presets.CarWheels(self.wheels,self.getDamping(),self.getDeflation())
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())
            
class MCFG_N_AnimationListPresetCarWheelsSteer(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - car steering wheels"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-list:-car-steering-wheels"
    
    # Node properties
    wheelFirst: bpy.props.IntProperty(
        name = "First",
        description = "First steerable wheel on one side",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 10
    )
    wheelLast: bpy.props.IntProperty(
        name = "Last",
        description = "Last steerable wheel on one side",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 10
    )
    angle: bpy.props.IntProperty(
        name = "Angle",
        description = "Maximal steering angle in degrees",
        default = 60,
        min = -360,
        max = 360,
        soft_min = -60,
        soft_max = 60
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
        box.label(text="Name: car steering wheels")
        box.prop(self, "wheelFirst")
        box.prop(self, "wheelLast")
        box.prop(self, "angle")
        
    # Custom functions
    def getRange(self):
        wheelRange = [self.wheelFirst,self.wheelLast]
        wheelRange.sort()
        
        return wheelRange
    
    def process(self):
        return Presets.CarWheelsSteer(self.getRange(),self.angle)
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())