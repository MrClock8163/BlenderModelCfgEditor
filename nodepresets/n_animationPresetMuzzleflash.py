import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets

class MCFG_N_AnimationPresetMuzzleflashRot(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - rotate muzzle flash"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-class:-rotate-muzzle-flash"
    
    # Node properties
    selectionName: bpy.props.StringProperty(
        default="zasleh",
        name="Selection",
        description = "Name of the selection to animate"
    )
    beginName: bpy.props.StringProperty(
        default="usti hlavne",
        name="Axis point 1",
        description = "Name of the first axis point"
    )
    endName: bpy.props.StringProperty(
        default="konec hlavne",
        name="Axis point 2",
        description = "Name of the second axis point"
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
        box.label(text="Name: muzzle flash rotation")
        box.prop(self, "selectionName")
        box.prop(self, "beginName")
        box.prop(self, "endName")
        
    # Custom functions
    def getSelection(self):        
        return self.selectionName.strip()
        
    def getAnimName(self):
        return (self.getSelection() + "_rot")
        
    def getAxis(self):
        return [self.beginName.strip(),self.endName.strip()]
        
    def process(self):
        return Presets.MuzzleflashRot(self.getAnimName(),self.getSelection(),self.getAxis())
        
    def inspect(self):
        data = self.process()
        print(data.Print())