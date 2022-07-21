import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data

class MCFG_N_Skeleton(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Skeleton class node'''
    
    # Mandatory variables
    bl_label = "Skeleton class"
    bl_icon = 'ARMATURE_DATA'
    
    # Custom variables
    node_group = "skeleton"
    process_type = "skeleton"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Skeleton-class"
    
    # Node properties
    skeletonName: bpy.props.StringProperty(
        default="Skeleton",
        name="Name",
        description = "Name of the skeleton class"
    )
    
    # Side panel properties
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
    
    # Standard functions
    def draw_label(self):
        return "Skeleton"
        
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
        
        self.unlinkInvalidSockets()
            
        if len(self.inputs[0].links) == 0:
            self.overrideIsDiscrete = True
            self.overrideInheritBones = True
            self.overrideBones = True
            
        if len(self.outputs[0].links) > 0:
            self.exportClass = True

    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_SkeletonParent', "Parent")
        self.inputs.new('MCFG_S_SkeletonParent', "Inherit bones")
        self.inputs.new('MCFG_S_ValueBool', "Discrete")
        self.inputs.new('MCFG_S_SkeletonBoneList', "Bone list")
        self.outputs.new('MCFG_S_SkeletonParent', "Out")

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.prop(self, "skeletonName")

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
        
    # Custom functions
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
        
        return self.inputs[2].links[0].from_node.process()
    
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
        
        if len(boneList) != 0 and (type(boneList[0]) != Data.Bone):
            return []
        
        return boneList
    
    def process(self):
        newSkeleton = Data.Skeleton(self.getSkeletonName(),self.getParentName())
        newSkeleton.Set("skeletonInherit",self.getInheritBones())
        newSkeleton.Set("isDiscrete",self.getDiscrete())
        newSkeleton.Set("skeletonBones",self.getBoneList())
        
        return newSkeleton
        
    def inspect(self):
        data = self.process()
        print(data.Print())
        
    def presetpostsettings(self):
        settings = []
        
        settings.append(["exportClass",self.exportClass])
        settings.append(["overrideBones",self.overrideBones])
        settings.append(["overrideIsDiscrete",self.overrideIsDiscrete])
        settings.append(["overrideInheritBones",self.overrideInheritBones])
        
        return settings