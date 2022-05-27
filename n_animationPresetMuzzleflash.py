import bpy
from bpy.types import Node
from . import n_tree
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_AnimationPresetMuzzleflashRot(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Animation item node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Animation class - rotate muzzle flash"
    # Icon identifier
    bl_icon = 'ANIM'
    
    node_group = "animation"
    animation_type = "translation"
    animation_type_min_value = "Offset0"
    animation_type_max_value = "Offset1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    


    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    
    
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
        box.label(text="Name: muzzle flash rotation")
        box.prop(self, "selectionName")
        box.prop(self, "beginName")
        box.prop(self, "endName")

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.label(text="Name: muzzle flash rotation")
        box.prop(self, "selectionName")
        box.prop(self, "beginName")
        box.prop(self, "endName")
    
    def getSelection(self):        
        return self.selectionName.strip()
        
    def getAnimName(self):
        return (self.getSelection() + "_rot")
        
    def getAxis(self):
        return [self.beginName.strip(),self.endName.strip()]
        
    def process(self):
        return Presets.MuzzleflashRot(self.getAnimName(),self.getSelection(),self.getAxis())

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Rotation preset"
        