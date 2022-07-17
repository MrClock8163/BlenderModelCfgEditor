import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data

class MCFG_N_Model(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Model class node'''
    
    # Mandatory variables
    bl_label = "Model class"
    bl_icon = 'OBJECT_DATA'
    
    # Custom variables
    node_group = "model"
    process_type = "model"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Model-class"
    
    # Node properties
    modelName: bpy.props.StringProperty(
        default="Model",
        name="Name",
        description = "Name of the model class\nNaming rules:\n-must be same as the name of the model P3D file\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    
    # Side panel properties
    def updateExportClass(self,context):
        if len(self.inputs) != 5:
            return
        
        if not self.exportClass:
            if len(self.outputs[0].links) > 0:
                for i in range(len(self.outputs[0].links)):
                    self.outputs[0].id_data.links.remove(self.outputs[0].links[0])
                self.exportClass = False
    
    def updateOverrideInheritSections(self,context):
        if len(self.inputs) != 5:
            return
        self.inputs[1].enabled = self.overrideInheritSections
        
        if (not self.overrideInheritSections) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideInheritSections:
            self.overrideInheritSections = True
            
    def updateOverrideSkeleton(self,context):
        if len(self.inputs) != 5:
            return
        self.inputs[2].enabled = self.overrideSkeleton
        
        if (not self.overrideSkeleton) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
        
        if len(self.inputs[0].links) == 0 and not self.overrideSkeleton:
            self.overrideSkeleton = True
            
    def updateOverrideSections(self,context):
        if len(self.inputs) != 5:
            return
        self.inputs[3].enabled = self.overrideSections
        
        if (not self.overrideSections) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSections:
            self.overrideSections = True
            
    def updateOverrideAnimations(self,context):
        if len(self.inputs) != 5:
            return
        
        if len(self.inputs[0].links) == 0 and self.overrideAnimations:
            self.overrideAnimations = False
    
    exportClass: bpy.props.BoolProperty(
        default = True,
        name = "Export",
        description = "Include this class in the exported config",
        update = updateExportClass
    )
    overrideInheritSections: bpy.props.BoolProperty(
        default=False,
        name="Inherit sections",
        update = updateOverrideInheritSections,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSkeleton: bpy.props.BoolProperty(
        default=False,
        name="Skeleton",
        update = updateOverrideSkeleton,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSections: bpy.props.BoolProperty(
        default=False,
        name="Sections",
        update = updateOverrideSections,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAnimations: bpy.props.BoolProperty(
        default=False,
        name="Animation",
        update = updateOverrideAnimations,
        description = "Inherit and/or override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideInheritSections = True
            self.overrideSkeleton = True
            self.overrideSections = True
            self.overrideAnimations = False
        
        if len(self.inputs) != 5:
            return
        
        if len(self.outputs[0].links) > 0:
            self.exportClass = True
    
    # Standard functions
    def draw_label(self):
        return "Model"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelParent', "Parent")
        self.inputs.new('MCFG_S_ModelParent', "Inherit sections")
        self.inputs.new('MCFG_S_SkeletonParent', "Skeleton")
        self.inputs.new('MCFG_S_ModelSectionList', "Section list")
        self.inputs.new('MCFG_S_ModelAnimationList', "Animation list")
        
        self.outputs.new('MCFG_S_ModelParent', "Out")

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "modelName")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "exportClass")
        box.prop(self, "modelName")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideInheritSections")
        box.prop(self, "overrideSkeleton")
        box.prop(self, "overrideSections")
        boxBounding.label(text="Inherit from parent:")
        box2 = boxBounding.box()
        box2.prop(self, "overrideAnimations")
        
    # Custom functions
    def getModelName(self):
        return self.modelName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getModelName()
        
    def getInheritSections(self):
        if not self.overrideInheritSections:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return ""
            
        return self.inputs[1].links[0].from_node.getModelName()
        
    def getSkeleton(self):
        if not self.overrideSkeleton:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return ""
            
        return self.inputs[2].links[0].from_node.getSkeletonName()
        
    def getSectionList(self):
        if not self.overrideSections:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return []
            
        sectionList = self.inputs[3].links[0].from_node.process()
        
        if len(sectionList) != 0 and (type(sectionList[0]) != str):
            return []
        
        return sectionList
        
    def getAnimationList(self):
        
        if len(self.inputs[4].links) == 0:
            return []
        
        animationList = self.inputs[4].links[0].from_node.process()
        
        if len(animationList) != 0 and (type(animationList[0]) != Data.Animation):
            return []
        
        return animationList
    
    def process(self):
        newModel = Data.Model(self.getModelName(),self.getParentName(),self.overrideAnimations)
        newModel.Set("sectionsInherit",self.getInheritSections())
        newModel.Set("skeletonName",self.getSkeleton())
        newModel.Set("sections",self.getSectionList())
        
        for anim in self.getAnimationList():
            newModel.AddAnim(anim)
        
        return newModel
        
    def inspect(self):
        data = self.process()
        print(data.Print())
        
    def presetpostsettings(self):
        settings = []
        
        settings.append(["exportClass",self.exportClass])
        settings.append(["overrideInheritSections",self.overrideInheritSections])
        settings.append(["overrideSkeleton",self.overrideSkeleton])
        settings.append(["overrideSections",self.overrideSections])
        settings.append(["overrideAnimations",self.overrideAnimations])
        
        return settings