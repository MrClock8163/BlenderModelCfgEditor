import bpy
from bpy.types import Node
from . import n_tree
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_AnimationListPresetBulletsHide(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Animation item node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Animation list - hide bullets"
    # Icon identifier
    bl_icon = 'ANIM'
    
    node_group = "animation"
    animation_type = "hide"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationnY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    
    selectionName: bpy.props.StringProperty(
        default="bullet_%",
        name="Selection name",
        description = "Name of the selection to animate\nMark the place for the generated index with a '%'"
    )
    animScope: bpy.props.EnumProperty(
        name = "Scope",
        description = "Whether the animation should affect a certain muzzle or any",
        default = 'ALL',
        items = (
            ('ALL',"Not muzzle specific","Animation affects any muzzles"),
            ('SPECIFIC',"Muzzle specific","Animation affects a specific muzzle")
        )
    )
    muzzleIndex: bpy.props.IntProperty(
        name = "Muzzle index",
        description = "Index of the muzzle to affect",
        default = 1,
        min = 1,
        max = 100,
        soft_max = 5
    )
    idlength: bpy.props.IntProperty(
        default=2,
        name = "ID length",
        description = "Length of the ID section of the generated bones\nWhere the ID number is fewer digits than this value, leading zeros are introduced\nWhen the value is lower than the digit count of the largest generated ID, that value is applied",
        min = 1,
        max = 50,
        soft_max = 5
    )
    
    magCapacity: bpy.props.IntProperty(
        name = "Magazine capacity",
        description = "Ammo capacity of the magazine",
        default = 20,
        min = 1,
        max = 1000,
        soft_max = 200
    )
    interval1: bpy.props.IntProperty(
        name = "First bullet",
        description = "Index of first bullet to be animated",
        default = 1,
        min = 1,
        max = 100
    )
    interval2: bpy.props.IntProperty(
        name = "Last bullet",
        description = "Index of last bullet to be animated",
        default = 1,
        min = 1,
        max = 100
    )
    
    
    def update(self):
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ModelAnimationList', "Animation list")

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
        box.label(text="Name: bullet hide")
        box.prop(self, "selectionName")
        box.prop(self, "animScope")
        if self.animScope == 'SPECIFIC':
            box.prop(self, "muzzleIndex")
        box.prop(self, "idlength")
        box.prop(self, "magCapacity")
        box.prop(self, "interval1")
        box.prop(self, "interval2")

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.label(text="Name: magazine hide")
        box.prop(self, "selectionName")
        box.prop(self, "animScope")
        if self.animScope == 'SPECIFIC':
            box.prop(self, "muzzleIndex")
        box.prop(self, "idlength")
        box.prop(self, "magCapacity")
        box.prop(self, "interval1")
        box.prop(self, "interval2")
    
    def getSelection(self):        
        return self.selectionName.strip()
        
    def getAnimName(self):
        return (self.getSelection() + "_rot")
    
    def getMuzzleIndex(self):
        if self.animScope == 'ALL':
            return -1
        else:
            return self.muzzleIndex - 1
        
    def process(self):
        return Presets.BulletHide(self.getSelection(),self.getMuzzleIndex(),self.idlength,self.magCapacity,[self.interval1,self.interval2])

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Hide preset"