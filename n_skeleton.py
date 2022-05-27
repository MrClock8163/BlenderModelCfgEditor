import bpy
from bpy.types import Node
from . import n_tree
from . import utility
from .utility import NodeInfo, InfoItem, InfoTypes
from . import utility_data as Data

class MCFG_N_Skeleton(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Skeleton class node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Skeleton class"
    # Icon identifier
    bl_icon = 'ARMATURE_DATA'
    
    node_group = "skeleton"
    export_type = "skeleton"

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    
    def updateOverrideBones(self,context):
        if len(self.inputs) != 4:
            return
        self.inputs[3].enabled = self.overrideBones
        
        if (not self.overrideBones) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        
        if len(self.inputs[0].links) == 0 and not self.overrideBones:
            self.overrideBones = True
            
    def updateOverrideIsDiscrete(self,context):
        if len(self.inputs) != 4:
            return
        self.inputs[2].enabled = self.overrideIsDiscrete
        
        if (not self.overrideIsDiscrete) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        
        if len(self.inputs[0].links) == 0 and not self.overrideIsDiscrete:
            self.overrideIsDiscrete = True
            
    def updateOverrideInheritBones(self,context):
        if len(self.inputs) != 4:
            return
        self.inputs[1].enabled = self.overrideInheritBones
        
        if (not self.overrideInheritBones) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        
        if len(self.inputs[0].links) == 0 and not self.overrideInheritBones:
            self.overrideInheritBones = True
    
    def updateExportClass(self, context):
        if len(self.inputs) != 4:
            return
        
        if not self.exportClass:
            if len(self.outputs[0].links) > 0:
                for i in range(len(self.outputs[0].links)):
                    self.outputs[0].id_data.links.remove(self.outputs[0].links[0])
                self.exportClass = False
                
    skeletonName: bpy.props.StringProperty(
        default="Skeleton",
        name="Name",
        description = "Name of the skeleton class\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    
    exportClass: bpy.props.BoolProperty(
        default = True,
        name = "Export",
        description = "Include this class in the exported config",
        update = updateExportClass
    )
    
    overrideBones: bpy.props.BoolProperty(
        default=False,
        name="Bones",
        update = updateOverrideBones,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideIsDiscrete: bpy.props.BoolProperty(
        default=False,
        name="Discrete",
        update = updateOverrideIsDiscrete,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideInheritBones: bpy.props.BoolProperty(
        default=False,
        name="Inherit bones",
        update = updateOverrideInheritBones,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
        
        self.unlinkInvalidSockets()
            
        if len(self.inputs[0].links) == 0:
            # print("Can't override")
            self.overrideIsDiscrete = True
            self.overrideInheritBones = True
            self.overrideBones = True
            
        if len(self.outputs[0].links) > 0:
            self.exportClass = True
    
    
    #my_float_prop: bpy.props.FloatProperty(default=3.1415926)

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        self.customColor()
        
        #self.inputs.new('CustomSocketType', "Hello")
        #self.inputs.new('NodeSocketFloat', "World")
        #self.inputs.new('NodeSocketVector', "!")
        self.inputs.new('MCFG_S_SkeletonParent', "Parent")
        self.inputs.new('MCFG_S_SkeletonParent', "Inherit bones")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "Discrete")
        self.inputs.new('MCFG_S_SkeletonBoneList', "Bone list")

        #self.outputs.new('NodeSocketColor', "How")
        #self.outputs.new('NodeSocketColor', "are")
        # self.outputs.new('ModelCfgSocketSkeletonOutput', "Skeleton output")
        self.outputs.new('MCFG_S_SkeletonParent', "Out")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        box = layout.box()
        box.prop(self, "skeletonName")
        
    def getSkeletonName(self):
        return self.skeletonName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getSkeletonName()
        
    def getDiscrete(self):
        
        if not self.overrideIsDiscrete:
            return '_HIDE_'
        
        if len(self.inputs[2].links) == 0:
            return self.inputs[2].getValue()
        
        
        return self.inputs[2].links[0].getValue()
    
    def getInheritBones(self):
        if not self.overrideInheritBones:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return ""
            
        return self.inputs[1].links[0].from_node.getSkeletonName()
        
    def getBoneList(self):
        if not self.overrideBones:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return []
            
        boneList = self.inputs[3].links[0].from_node.process()
        
        
        return boneList
    
    def process(self):
        newSkeleton = Data.Skeleton(self.getSkeletonName(),self.getParentName())
        newSkeleton.Set("skeletonInherit",self.getInheritBones())
        newSkeleton.Set("isDiscrete",self.getDiscrete())
        newSkeleton.Set("skeletonBones",self.getBoneList())
        
        return newSkeleton
   

    # Detail buttons in the sidebar.
    # If this function is not defined, the draw_buttons function is used instead
    # If this function is not defined, the draw_buttons function is used instead
    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.prop(self, "exportClass")
        box.prop(self, "skeletonName")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideInheritBones")
        box.prop(self, "overrideIsDiscrete")
        box.prop(self, "overrideBones")
        # my_string_prop button will only be visible in the sidebar

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Skeleton"