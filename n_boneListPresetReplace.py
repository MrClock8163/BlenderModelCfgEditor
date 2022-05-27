import bpy
from bpy.types import Node
from . import n_tree
from . import utility_data as Data
from . import utility_presets as Presets

class MCFG_N_BoneListPresetReplace(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Bone list nod'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Bone list - replace"
    # Icon identifier
    bl_icon = 'ANIM'
    
    node_group = "bone"
    
    searchFor: bpy.props.StringProperty(
        default="right",
        name="Replace",
        description = "Bone name part to replace"
    )
    replaceWith: bpy.props.StringProperty(
        default = "left",
        name = "With",
        description = "String to replace the search string with"
    )
    result: bpy.props.EnumProperty(
        name = "Filter",
        description = "The result the node should return",
        default = 'FULL',
        items = (
            ('FULL',"Full list","Return a list of all bones"),
            ('CHANGED',"Only the changed","Return a list of the bones that had their names changed only")
        )
    )
    operation: bpy.props.EnumProperty(
        name = "Operation",
        description = "How to operate on the list",
        default = 'COPY',
        items = (
            ('REPLACE',"Replace","Replace specified parts in the names of the bones in the given list"),
            ('COPY',"Copy and replace","Copy the list and replace specified parts in the names of the bones in the copied list")
        )
    )
    
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        self.inputs.new('MCFG_S_SkeletonBoneList', "Bone list")
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
        box.label(text="Name: search and replace")
        box.prop(self, "searchFor")
        box.prop(self, "replaceWith")
        box.prop(self, "result")
        if self.result == 'FULL':
            box.prop(self, "operation")
            

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.label(text="Name: search and replace")
        box.prop(self, "searchFor")
        box.prop(self, "replaceWith")
        box.prop(self, "result")
        if self.result == 'FULL':
            box.prop(self, "operation")
    
            
    def getBoneList(self):
        if len(self.inputs[0].links) == 0:
            return []
            
        boneList = self.inputs[0].links[0].from_node.process()
        return boneList
        
    def process(self):
        return Presets.BoneReplace(self.getBoneList(),self.searchFor,self.replaceWith,self.result,self.operation)

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Bone preset"