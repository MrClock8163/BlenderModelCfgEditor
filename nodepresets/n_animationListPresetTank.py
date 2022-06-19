import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationListPresetTank(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation list node'''
    
    # Mandatory variables
    bl_label = "Animation list - tank wheels"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-list:-tank-wheels"
    
    # Node properties
    wheelFixed: bpy.props.IntProperty(
        name = "Fixed",
        description = "Number of not suspended wheels",
        default = 2,
        min = 0,
        max = 100,
        soft_max = 5
    )
    wheelDamping: bpy.props.IntProperty(
        name = "Suspended",
        description = "Number of suspended wheels",
        default = 5,
        min = 0,
        max = 100,
        soft_max = 10
    )
    dampMin: bpy.props.FloatProperty(
        name = "Compress",
        description = "Maximal damper compression offset from startion position",
        default = 0.2,
        min = 0,
        max = 100,
        soft_max = 1
    )
    dampMax: bpy.props.FloatProperty(
        name = "Expand",
        description = "Maximal damper expansion offset from startion position",
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
        box.label(text="Name: tank wheels")
        box.prop(self, "wheelFixed")
        box.prop(self, "wheelDamping")
        if self.wheelDamping > 0:
            box.prop(self, "dampMin")
            box.prop(self, "dampMax")
        
    # Custom functions    
    def getDamping(self):
        dampRange = [round(-self.dampMin,6),round(self.dampMax,6)]
        dampRange.sort()
        
        return dampRange
    
    def process(self):
        return Presets.TankWheels(self.wheelFixed,self.wheelDamping,self.getDamping())
        
    def inspect(self):
        for anim in self.process():
            print(anim.Print())