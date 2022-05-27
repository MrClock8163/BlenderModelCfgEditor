import bpy
from bpy.types import Node
from . import n_tree
from . import utility
from .utility import NodeInfo, InfoItem, InfoTypes
from . import utility_data as Data

class MCFG_N_Model(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Model class node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Model class"
    # Icon identifier
    bl_icon = 'OBJECT_DATA'
    
    node_group = "model"
    export_type = "model"
    

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    
    modelName: bpy.props.StringProperty(
        default="Model",
        name="Name",
        description = "Name of the model class\nNaming rules:\n-must be same as the name of the model P3D file\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    
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
        # self.inputs[3].enabled = self.overrideAnimations
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
    
    def update(self):
        if len(self.inputs) == 0 or len(self.outputs) == 0:
            return
            
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            # print("Can't override")
            self.overrideInheritSections = True
            self.overrideSkeleton = True
            self.overrideSections = True
            self.overrideAnimations = False
        
        if len(self.inputs) != 5:
            return
        self.inputs[4].enabled = (len(self.inputs[2].links) != 0 or (not self.overrideSkeleton))
        
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
        
        self.inputs.new('MCFG_S_ModelParent', "Parent")
        self.inputs.new('MCFG_S_ModelParent', "Inherit sections")
        self.inputs.new('MCFG_S_SkeletonParent', "Skeleton")
        self.inputs.new('MCFG_S_ModelSectionList', "Section list")
        self.inputs.new('MCFG_S_ModelAnimationList', "Animation list")
        
        
        self.outputs.new('MCFG_S_ModelParent', "Out")

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
        # box.prop(self, "exportClass")
        box.prop(self, "modelName")

    # Detail buttons in the sidebar.
    # If this function is not defined, the draw_buttons function is used instead
    def draw_buttons_ext(self, context, layout):
    
    
        # MEG KÉNE PRÓBÁLNI BOX()-BA RENDEZNI ŐKET MINT A BEÁLLÍTÁSOKBAN
        
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
    
    
        #layout.prop(self, "my_float_prop")
        # my_string_prop button will only be visible in the sidebar

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
        
        
        return sectionList
        
    def getAnimationList(self):
        
        if len(self.inputs[4].links) == 0:
            return []
        
        animationList = self.inputs[4].links[0].from_node.process()
        
        return animationList
    
    def process(self):
        newModel = Data.Model(self.getModelName(),self.getParentName(),self.overrideAnimations)
        newModel.Set("sectionsInherit",self.getInheritSections())
        newModel.Set("skeletonName",self.getSkeleton())
        newModel.Set("sections",self.getSectionList())
        
        for anim in self.getAnimationList():
            newModel.AddAnim(anim)
        
        return newModel
        

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Model"