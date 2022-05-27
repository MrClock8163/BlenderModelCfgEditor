import bpy
from bpy.types import Node
from . import n_tree
from . import utility_data as Data

class MCFG_N_AnimationTranslation(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - translation"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "translation"
    animation_type_min_value = "Offset0"
    animation_type_max_value = "Offset1"
    incompatible_nodes = ["MCFG_N_AnimationRotation","MCFG_N_AnimationRotationX","MCFG_N_AnimationRotationY","MCFG_N_AnimationRotationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12: # inputs are not yet initialized
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Translation"
        
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True
    
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        if len(self.inputs[10].links) == 0:
            return round(self.inputs[10].floatValue,6)
            
        return self.inputs[10].links[0].from_node.process()
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[11].links) == 0:
            return round(self.inputs[11].floatValue,6)
            
        return self.inputs[11].links[0].from_node.process()
        
    def process(self):
        animType = '_HIDE_'
        
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim
        
class MCFG_N_AnimationTranslationX(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - translation X"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "translationX"
    animation_type_min_value = "Offset0"
    animation_type_max_value = "Offset1"
    incompatible_nodes = ["MCFG_N_AnimationRotation","MCFG_N_AnimationRotationX","MCFG_N_AnimationRotationY","MCFG_N_AnimationRotationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12: # inputs are not yet initialized
            return

        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Translation X"
        
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True
    
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
    
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        if len(self.inputs[10].links) == 0:
            return round(self.inputs[10].floatValue,6)
            
        return self.inputs[10].links[0].from_node.process()
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[11].links) == 0:
            return round(self.inputs[11].floatValue,6)
            
        return self.inputs[11].links[0].from_node.process()
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim
        
class MCFG_N_AnimationTranslationY(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''

    # Mandatory variables
    bl_label = "Animation class - translation Y"
    bl_icon = 'ANIM'
        
    # Custom variables
    node_group = "animation"
    animation_type = "translationY"
    animation_type_min_value = "Offset0"
    animation_type_max_value = "Offset1"
    incompatible_nodes = ["MCFG_N_AnimationRotation","MCFG_N_AnimationRotationX","MCFG_N_AnimationRotationY","MCFG_N_AnimationRotationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12: # inputs are not yet initialized
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Translation Y"
    
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True

    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        if len(self.inputs[10].links) == 0:
            return round(self.inputs[10].floatValue,6)
            
        return self.inputs[10].links[0].from_node.process()
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[11].links) == 0:
            return round(self.inputs[11].floatValue,6)
            
        return self.inputs[11].links[0].from_node.process()
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim
                
class MCFG_N_AnimationTranslationZ(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''

    # Mandatory variables
    bl_label = "Animation class - translation Z"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "translationZ"
    animation_type_min_value = "Offset0"
    animation_type_max_value = "Offset1"
    incompatible_nodes = ["MCFG_N_AnimationRotation","MCFG_N_AnimationRotationX","MCFG_N_AnimationRotationY","MCFG_N_AnimationRotationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12: # inputs are not yet initialized
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )

    # Standard functions
    def draw_label(self):
        return "Translation Z"
        
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True

    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        if len(self.inputs[10].links) == 0:
            return round(self.inputs[10].floatValue,6)
            
        return self.inputs[10].links[0].from_node.process()
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[11].links) == 0:
            return round(self.inputs[11].floatValue,6)
            
        return self.inputs[11].links[0].from_node.process()
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim

class MCFG_N_AnimationRotation(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - rotation"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "rotation"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12: # inputs are not yet initialized
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    angleType: bpy.props.EnumProperty(
        name = "Angle unit",
        default = 'DEG',
        items = (
            ('DEG',"Degrees","The angles are input in degrees"),
            ('RAD',"Radians","The angles are input in radians")
        ),
        description = "Options to set how to treat the angle values. Since arma expects radians, if the input is in degrees, a necessary transformation is done upon export."
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Rotation"
        
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True
    
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")

    def draw_buttons_ext(self, context, layout):
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[10].links) == 0:
            returnAngle = round(self.inputs[10].floatValue,6)
        else:
            returnAngle = self.inputs[10].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[11].links) == 0:
            returnAngle = round(self.inputs[11].floatValue,6)
        else:
            returnAngle = self.inputs[11].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim

class MCFG_N_AnimationRotationX(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - rotation X"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "rotationX"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12:
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    angleType: bpy.props.EnumProperty(
        name = "Angle unit",
        default = 'DEG',
        items = (
            ('DEG',"Degrees","The angles are input in degrees"),
            ('RAD',"Radians","The angles are input in radians")
        ),
        description = "Options to set how to treat the angle values. Since arma expects radians, if the input is in degrees, a necessary transformation is done upon export."
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Rotation X"
    
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True

    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[10].links) == 0:
            returnAngle = round(self.inputs[10].floatValue,6)
        else:
            returnAngle = self.inputs[10].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[11].links) == 0:
            returnAngle = round(self.inputs[11].floatValue,6)
        else:
            returnAngle = self.inputs[11].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim
        
class MCFG_N_AnimationRotationY(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - rotation Y"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "rotationY"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12:
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    angleType: bpy.props.EnumProperty(
        name = "Angle unit",
        default = 'DEG',
        items = (
            ('DEG',"Degrees","The angles are input in degrees"),
            ('RAD',"Radians","The angles are input in radians")
        ),
        description = "Options to set how to treat the angle values. Since arma expects radians, if the input is in degrees, a necessary transformation is done upon export."
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Rotation Y"
        
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True

    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
    
    def Validate(self,errors):
        errorList = []
        
        if not utility.ValidName(self.animName):
            errorList.append("Animation name is invalid")
        
        if len(errorList) != 0:
            errors.append(errorList)
            
        return errors
        
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[10].links) == 0:
            returnAngle = round(self.inputs[10].floatValue,6)
        else:
            returnAngle = self.inputs[10].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[11].links) == 0:
            returnAngle = round(self.inputs[11].floatValue,6)
        else:
            returnAngle = self.inputs[11].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim
                
class MCFG_N_AnimationRotationZ(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - rotation Z"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "rotationZ"
    animation_type_min_value = "Angle0"
    animation_type_max_value = "Angle1"
    incompatible_nodes = ["MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationY","MCFG_N_AnimationTranslationZ","MCFG_N_AnimationHide"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12:
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    angleType: bpy.props.EnumProperty(
        name = "Angle unit",
        default = 'DEG',
        items = (
            ('DEG',"Degrees","The angles are input in degrees"),
            ('RAD',"Radians","The angles are input in radians")
        ),
        description = "Options to set how to treat the angle values. Since arma expects radians, if the input is in degrees, a necessary transformation is done upon export."
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Rotation Z"
    
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            self.overrideMemory = True
            self.overrideAxis = True
            self.overrideBegin = True
            self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True

    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "axisType")
        box.prop(self, "angleType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        box.prop(self, "overrideMemory")
        box.prop(self, "overrideAxis")
        box.prop(self, "overrideBegin")
        box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[10].links) == 0:
            returnAngle = round(self.inputs[10].floatValue,6)
        else:
            returnAngle = self.inputs[10].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        returnAngle = 0
        if len(self.inputs[11].links) == 0:
            returnAngle = round(self.inputs[11].floatValue,6)
        else:
            returnAngle = self.inputs[11].links[0].from_node.process()
        
        if self.angleType == 'DEG':
            returnAngle = returnAngle * (3.141592653589793/180)
            
        return returnAngle
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",self.getMemory())
        axisData = self.getAxis()
        newAnim.Set("axis",axisData[0])
        newAnim.Set("begin",axisData[1])
        newAnim.Set("end",axisData[2])
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim
        
class MCFG_N_AnimationHide(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class - hide"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    animation_type = "hide"
    animation_type_min_value = "hideValue"
    animation_type_max_value = "unhideValue"
    incompatible_nodes = ["MCFG_N_AnimationRotation","MCFG_N_AnimationRotationX","MCFG_N_AnimationRotationY","MCFG_N_AnimationRotationZ","MCFG_N_AnimationTranslation","MCFG_N_AnimationTranslationX","MCFG_N_AnimationTranslationY","MCFG_N_AnimationTranslationZ"]
    
    # Node properties
    def updateAxisType(self, context):
        if len(self.inputs) != 12:
            return
        
        if self.axisType == 'AXIS':
            self.inputs[5].enabled = self.overrideAxis
            self.inputs[6].reset()
            self.inputs[6].enabled = False
            self.inputs[7].reset()
            self.inputs[7].enabled = False
        else:
            self.inputs[5].reset()
            self.inputs[5].enabled = False
            self.inputs[6].enabled = self.overrideBegin
            self.inputs[7].enabled = self.overrideEnd
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters\n-no whitespaces"
    )
    axisType: bpy.props.EnumProperty(
        name = "Axis",
        default = 'AXIS',
        items = (
            ('AXIS',"Axis","The axis of transformation is set to be an axis selection"),
            ('POINTS',"Two points","The axis of transformation is defined by two points")
        ),
        update = updateAxisType,
        description = "Options to set how the transformation axis is defined in the model's memory LOD"
    )
    
    # Side panel properties
    def updateOverrideSource(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[1].enabled = self.overrideSource
        
        if (not self.overrideSource) and len(self.inputs[1].links) != 0:
            self.inputs[1].id_data.links.remove(self.inputs[1].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSource:
            self.overrideSource = True
    
    def updateOverrideSourceAddress(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[2].enabled = self.overrideSourceAddress
        
        if (not self.overrideSourceAddress) and len(self.inputs[2].links) != 0:
            self.inputs[2].id_data.links.remove(self.inputs[2].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSourceAddress:
            self.overrideSourceAddress = True
    
    def updateOverrideSelection(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[3].enabled = self.overrideSelection
        
        if (not self.overrideSelection) and len(self.inputs[3].links) != 0:
            self.inputs[3].id_data.links.remove(self.inputs[3].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideSelection:
            self.overrideSelection = True
    
    def updateOverrideMemory(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[4].enabled = self.overrideMemory
        
        if (not self.overrideMemory) and len(self.inputs[4].links) != 0:
            self.inputs[4].id_data.links.remove(self.inputs[4].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMemory:
            self.overrideMemory = True
    
    def updateOverrideAxis(self, context):
        if len(self.inputs) != 12:
            return
        
        self.inputs[5].enabled = self.overrideAxis and self.axisType == 'AXIS'
        
        if (not self.overrideAxis) and len(self.inputs[5].links) != 0:
            self.inputs[5].id_data.links.remove(self.inputs[5].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideAxis:
            self.overrideAxis = True
    
    def updateOverrideBegin(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[6].enabled = self.overrideBegin and self.axisType == 'POINTS'
        
        if (not self.overrideBegin) and len(self.inputs[6].links) != 0:
            self.inputs[6].id_data.links.remove(self.inputs[6].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideBegin:
            self.overrideBegin = True
    
    def updateOverrideEnd(self, context):
        if len(self.inputs) != 12:
            return
            
        self.inputs[7].enabled = self.overrideEnd and self.axisType == 'POINTS'
        
        if (not self.overrideEnd) and len(self.inputs[7].links) != 0:
            self.inputs[7].id_data.links.remove(self.inputs[7].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideEnd:
            self.overrideEnd = True
    
    def updateOverrideMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[8].enabled = self.overrideMinValue
        
        if (not self.overrideMinValue) and len(self.inputs[8].links) != 0:
            self.inputs[8].id_data.links.remove(self.inputs[8].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMinValue:
            self.overrideMinValue = True
    
    def updateOverrideMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[9].enabled = self.overrideMaxValue
        
        if (not self.overrideMaxValue) and len(self.inputs[9].links) != 0:
            self.inputs[9].id_data.links.remove(self.inputs[9].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideMaxValue:
            self.overrideMaxValue = True
    
    def updateOverrideTypeMinValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[10].enabled = self.overrideTypeMinValue
        
        if (not self.overrideTypeMinValue) and len(self.inputs[10].links) != 0:
            self.inputs[10].id_data.links.remove(self.inputs[10].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMinValue:
            self.overrideTypeMinValue = True
    
    def updateOverrideTypeMaxValue(self, context):
        if len(self.inputs) != 12:
            return
        self.inputs[11].enabled = self.overrideTypeMaxValue
        
        if (not self.overrideTypeMaxValue) and len(self.inputs[11].links) != 0:
            self.inputs[11].id_data.links.remove(self.inputs[11].links[0])
            
        if len(self.inputs[0].links) == 0 and not self.overrideTypeMaxValue:
            self.overrideTypeMaxValue = True
    
    overrideSource: bpy.props.BoolProperty(
        default = False,
        name = "Source",
        update = updateOverrideSource,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSourceAddress: bpy.props.BoolProperty(
        default = False,
        name = "Source address",
        update = updateOverrideSourceAddress,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideSelection: bpy.props.BoolProperty(
        default = False,
        name = "Selection",
        update = updateOverrideSelection,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMemory: bpy.props.BoolProperty(
        default = False,
        name = "Memory",
        update = updateOverrideMemory,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideAxis: bpy.props.BoolProperty(
        default = False,
        name = "Axis",
        update = updateOverrideAxis,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideBegin: bpy.props.BoolProperty(
        default = False,
        name = "Begin",
        update = updateOverrideBegin,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideEnd: bpy.props.BoolProperty(
        default = False,
        name = "End",
        update = updateOverrideEnd,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Min value",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Max value",
        update = updateOverrideMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMinValue: bpy.props.BoolProperty(
        default = False,
        name = "Type min value",
        update = updateOverrideTypeMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideTypeMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Type max value",
        update = updateOverrideTypeMaxValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    
    # Standard functions
    def draw_label(self):
        return "Hide"
    
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            # self.overrideMemory = True
            # self.overrideAxis = True
            # self.overrideBegin = True
            # self.overrideEnd = True
            self.overrideMinValue = True
            self.overrideMaxValue = True
            self.overrideTypeMinValue = True
            self.overrideTypeMaxValue = True

    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelAnimation', "Parent")
        self.inputs.new('MCFG_S_ValueString', "source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "sourceAddress")
        self.inputs.new('MCFG_S_ValueString', "selection")
        self.inputs.new('MCFG_S_SkeletonIsDiscrete', "memory")
        self.inputs.new('MCFG_S_ValueString', "axis")
        self.inputs.new('MCFG_S_ValueString', "begin")
        self.inputs.new('MCFG_S_ValueString', "end")
        self.inputs.new('MCFG_S_ValueFloat', "minValue")
        self.inputs.new('MCFG_S_ValueFloat', "maxValue")
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_min_value)
        self.inputs.new('MCFG_S_ValueFloat', self.animation_type_max_value)
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[4].enabled = False
        self.inputs[5].enabled = False
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        # box.prop(self, "axisType")
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        # box.prop(self, "overrideMemory")
        # box.prop(self, "overrideAxis")
        # box.prop(self, "overrideBegin")
        # box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue",text=self.animation_type_min_value)
        box.prop(self, "overrideTypeMaxValue",text=self.animation_type_max_value)

    def copy(self, node):
        print("Copying from node ", node)

    def free(self):
        print("Removing node ", self, ", Goodbye!")
        
    # Custom functions
    def getAnimName(self):
        return self.animName.strip()
        
    def getParentName(self):
        if len(self.inputs[0].links) == 0:
            return ""
            
        return self.inputs[0].links[0].from_node.getAnimName()
        
    def getSource(self):
        if not self.overrideSource:
            return '_HIDE_'
    
        if len(self.inputs[1].links) == 0:
            return self.inputs[1].stringValue.strip()
            
        return self.inputs[1].links[0].from_node.process()
        
    def getSourceAddress(self):
        if not self.overrideSourceAddress:
            return '_HIDE_'
    
        if len(self.inputs[2].links) == 0:
            return str(self.inputs[2].typeValue).lower()
            
        return self.inputs[2].links[0].from_node.process()
        
    def getSelection(self):
        if not self.overrideSelection:
            return '_HIDE_'
    
        if len(self.inputs[3].links) == 0:
            return self.inputs[3].stringValue.strip()
            
        selection = self.inputs[3].links[0].from_node.process()
        
        if isinstance(selection,Data.Bone):
            selection = selection.name
        
        return selection
        
    def getMemory(self):
        if not self.overrideMemory:
            return '_HIDE_'
    
        if len(self.inputs[4].links) == 0:
            return self.inputs[4].getValue()
            
        return self.inputs[4].links[0].from_node.process()
        
    def getAxis(self):
        axisValue = '_HIDE_'
        beginValue = '_HIDE_'
        endValue = '_HIDE_'
        
        if self.inputs[5].enabled:
            if len(self.inputs[5].links) == 0:
                axisValue = self.inputs[5].stringValue.strip()
            else:
                axisValue = self.inputs[5].links[0].from_node.process()
        
        if self.inputs[6].enabled:
            if len(self.inputs[6].links) == 0:
                beginValue = self.inputs[6].stringValue.strip()
            else:
                beginValue = self.inputs[6].links[0].from_node.process()
        
        if self.inputs[7].enabled:
            if len(self.inputs[7].links) == 0:
                endValue = self.inputs[7].stringValue.strip()
            else:
                endValue = self.inputs[7].links[0].from_node.process()
            
        return [axisValue,beginValue,endValue]
        
    def getMinValue(self):
        if not self.overrideMinValue:
            return '_HIDE_'
    
        if len(self.inputs[8].links) == 0:
            return round(self.inputs[8].floatValue,6)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return round(self.inputs[9].floatValue,6)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
    
        if len(self.inputs[10].links) == 0:
            return round(self.inputs[10].floatValue,6)
            
        return self.inputs[10].links[0].from_node.process()
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[11].links) == 0:
            return round(self.inputs[11].floatValue,6)
            
        return self.inputs[11].links[0].from_node.process()
        
    def process(self):
        animType = '_HIDE_'
        if self.getParentName() == "":
            animType = self.animation_type
    
        newAnim = Data.Animation(self.getAnimName(),animType,self.getParentName())
        newAnim.Set("source",self.getSource())
        newAnim.Set("sourceAddress",self.getSourceAddress())
        newAnim.Set("selection",self.getSelection())
        newAnim.Set("memory",-1)
        newAnim.Set("axis",-1)
        newAnim.Set("begin",-1)
        newAnim.Set("end",-1)
        newAnim.Set("minValue",self.getMinValue())
        newAnim.Set("maxValue",self.getMaxValue())
        newAnim.Set("typeMinValue",self.getMinTypeValue())
        newAnim.Set("typeMaxValue",self.getMaxTypeValue())
        
        return newAnim