import bpy
from bpy.types import Node
from . import n_tree
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_BoneListPresetSymmetrize(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Bone list nod'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Bone list - symmetrize"
    # Icon identifier
    bl_icon = 'ANIM'
    
    node_group = "bone"
    
    stringLeft: bpy.props.StringProperty(
        default="_left",
        name="Left",
        description = "Suffix to add to left side bones"
    )
    stringRight: bpy.props.StringProperty(
        default = "_right",
        name = "Right",
        description = "Suffix to add to right side bones"
    )
    
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.inputs.new('MCFG_S_SkeletonBoneList', "Base bone list")
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

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
        box.label(text="Name: symmetrize")
        box.prop(self, "stringLeft")
        box.prop(self, "stringRight")
            

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.label(text="Name: symmetrize")
        box.prop(self, "stringLeft")
        box.prop(self, "stringRight")
    
            
    def getBoneList(self):
        if len(self.inputs[0].links) == 0:
            return []
            
        boneList = self.inputs[0].links[0].from_node.process()
        return boneList
        
    def process(self):
        return Presets.BoneSymmetrize(self.getBoneList(),self.stringLeft,self.stringRight)

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Bone preset"