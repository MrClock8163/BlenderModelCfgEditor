import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_presets as Presets
from .. import utility_data as Data

class MCFG_N_BoneListPresetReplace(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Bone list node'''
    
    # Mandatory variables
    bl_label = "Bone list - replace"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "bone"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Bone-list:-replace"
    
    # Node properties
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
    
    # Standard functions
    def draw_label(self):
        return "Bone preset"
        
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
    
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_SkeletonBoneList', "Bone list")
        self.outputs.new('MCFG_S_SkeletonBoneList', "Bone list")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text="Name: search and replace")
        box.prop(self, "searchFor")
        box.prop(self, "replaceWith")
        box.prop(self, "result")
        if self.result == 'FULL':
            box.prop(self, "operation")
        
    # Custom functions
    def getBoneList(self):
        if len(self.inputs[0].links) == 0:
            return []
            
        boneList = self.inputs[0].links[0].from_node.process()
        
        if len(boneList) != 0 and (type(boneList[0]) != Data.Bone):
            return []
        
        return boneList
        
    def process(self):
        return Presets.BoneReplace(self.getBoneList(),self.searchFor,self.replaceWith,self.result,self.operation)
        
    def inspect(self):
        for bone in self.process():
            print(bone)