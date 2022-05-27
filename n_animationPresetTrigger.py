import bpy
from bpy.types import Node
from . import n_tree
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_AnimationPresetTriggerRot(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Animation item node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Animation class - rotate trigger"
    # Icon identifier
    bl_icon = 'ANIM'
    
    node_group = "animation"
    animation_type = "rotation"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    
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
    
    
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        # layout.label(text="Node settings")
        box = layout.box()
        box.label(text="Name: trigger rotation")
        box.prop(self, "selectionName")
        box.prop(self, "axisName")
        box.prop(self, "rotationLimit")

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.label(text="Name: trigger rotation")
        box.prop(self, "selectionName")
        box.prop(self, "axisName")
        box.prop(self, "rotationLimit")
    
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

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Rotation preset"

class MCFG_N_AnimationPresetTriggerMove(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Animation item node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Animation class - move trigger"
    # Icon identifier
    bl_icon = 'ANIM'
    
    node_group = "animation"
    animation_type = "translation"
    animation_type_min_value = "Offset0"
    animation_type_max_value = "Offset1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    
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
    
    
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        # layout.label(text="Node settings")
        box = layout.box()
        box.label(text="Name: trigger translation")
        box.prop(self, "selectionName")
        box.prop(self, "axisName")
        box.prop(self, "translationLimit")

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.label(text="Name: trigger translation")
        box.prop(self, "selectionName")
        box.prop(self, "axisName")
        box.prop(self, "translationLimit")
    
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

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Translation preset"
        