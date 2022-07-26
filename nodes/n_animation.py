import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility as Utils
from .. import utility_data as Data

class MCFG_N_Animation(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Animation item node'''
    
    # Mandatory variables
    bl_label = "Animation class"
    bl_icon = 'ANIM'
    
    # Custom variables
    node_group = "animation"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Animation-class"
    
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
    
    def updateAnimType(self, context):
        if len(self.inputs) != 12:
            return
            
        if self.animType == 'HIDE':
            self.inputs[4].enabled = False
            self.inputs[5].enabled = False
            self.inputs[6].enabled = False
            self.inputs[7].enabled = False
            
            self.inputs[10].name = "Hide threshold"
            self.inputs[11].name = "Unhide threshold"
        else:
            self.inputs[4].enabled = True
            self.inputs[5].enabled = True
            self.inputs[6].enabled = True
            self.inputs[7].enabled = True
            self.updateAxisType(context)
            
            if self.animType in ['TRANSLATION','TRANSLATIONX','TRANSLATIONY','TRANSLATIONZ']:
                self.inputs[10].name = "Starting offset"
                self.inputs[11].name = "Target offset"
            elif self.animType in ['ROTATION','ROTATIONX','ROTATIONY','ROTATIONZ']:
                self.inputs[10].name = "Starting angle"
                self.inputs[11].name = "Target angle"
    
    def updateAnimName(self,context):
        self.name = "Animation: {}".format(self.animName)
    
    animName: bpy.props.StringProperty(
        default="Animation",
        name="Name",
        description = "Name of the animation",
        update = updateAnimName
    )
    animType: bpy.props.EnumProperty(
        name = "Animation type",
        default = 'TRANSLATION',
        items = (
            ('TRANSLATION',"Translation","Translation along a generic axis in the model space"),
            ('TRANSLATIONX',"Translation X","Translation along the X axis in the model space"),
            ('TRANSLATIONY',"Translation Y","Translation along the Y axis in the model space"),
            ('TRANSLATIONZ',"Translation Z","Translation along the Z axis in the model space"),
            ('ROTATION',"Rotation","Rotation around a generic axis in the model space"),
            ('ROTATIONX',"Rotation X","Rotation around the X axis in the model space"),
            ('ROTATIONY',"Rotation Y","Rotation around the Y axis in the model space"),
            ('ROTATIONZ',"Rotation Z","Rotation around the Z axis in the model space"),
            ('HIDE',"Hide","Hide selection")
        ),
        description = "Type of the animation",
        update = updateAnimType
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
        name = "Source phase range start",
        update = updateOverrideMinValue,
        description = "Override the value from the parent class (only allowed if parent class is specified)"
    )
    overrideMaxValue: bpy.props.BoolProperty(
        default = False,
        name = "Source phase range end",
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
        
        if self.animType in ['TRANSLATION','TRANSLATIONX','TRANSLATIONY','TRANSLATIONZ']:
            return "Translation"
        elif self.animType in ['ROTATION','ROTATIONX','ROTATIONY','ROTATIONZ']:
            return "Rotation"
        elif self.animType == 'HIDE':
            return "Hide"
        
    def update(self):
        self.unlinkInvalidSockets()
        if len(self.inputs[0].links) == 0:
            self.overrideSource = True
            self.overrideSourceAddress = True
            self.overrideSelection = True
            if self.animType != 'HIDE':
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
        self.inputs.new('MCFG_S_ValueString', "Source")
        self.inputs.new('MCFG_S_ModelSourceAddress', "Source limit")
        self.inputs.new('MCFG_S_ValueString', "Selection")
        self.inputs.new('MCFG_S_ValueBool', "Memory")
        self.inputs.new('MCFG_S_ValueString', "Axis")
        self.inputs.new('MCFG_S_ValueString', "Begin")
        self.inputs.new('MCFG_S_ValueString', "End")
        self.inputs.new('MCFG_S_ValueFloat', "Source phase range start")
        self.inputs.new('MCFG_S_ValueFloat', "Source phase range end")
        self.inputs.new('MCFG_S_ValueFloat', "typeMinValue")
        self.inputs.new('MCFG_S_ValueFloat', "typeMaxValue")
        self.outputs.new('MCFG_S_ModelAnimation', "Animation")
        
        self.inputs[6].enabled = False
        self.inputs[7].enabled = False
        
        self.inputs[9].floatValue = 1.0
        self.inputs[11].floatValue = 1.0
        
        self.updateAnimType(context)

    def draw_buttons(self, context, layout): # Node properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "animType",text="Type")
        if self.animType != 'HIDE':
            box.prop(self, "axisType",icon='EMPTY_AXIS')

    def draw_buttons_ext(self, context, layout): # Side panel properties
        box = layout.box()
        box.prop(self, "animName")
        box.prop(self, "animType",text="Type")
        if self.animType != 'HIDE':
            box.prop(self, "axisType",icon='EMPTY_AXIS')
        boxBounding = layout.box()
        boxBounding.label(text="Override parent:")
        box = boxBounding.box()
        box.prop(self, "overrideSource")
        box.prop(self, "overrideSourceAddress")
        box.prop(self, "overrideSelection")
        if self.animType != 'HIDE':
            box.prop(self, "overrideMemory")
            box.prop(self, "overrideAxis")
            box.prop(self, "overrideBegin")
            box.prop(self, "overrideEnd")
        box.prop(self, "overrideMinValue")
        box.prop(self, "overrideMaxValue")
        box.prop(self, "overrideTypeMinValue")
        box.prop(self, "overrideTypeMaxValue")
        
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
            return Utils.FloatValue(self.inputs[8].floatValue,self.inputs[8].isDeg)
            
        return self.inputs[8].links[0].from_node.process()
        
    def getMaxValue(self):
        if not self.overrideMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[9].links) == 0:
            return Utils.FloatValue(self.inputs[9].floatValue,self.inputs[9].isDeg)
            
        return self.inputs[9].links[0].from_node.process()
        
    def getMinTypeValue(self):
        if not self.overrideTypeMinValue:
            return '_HIDE_'
        
        if len(self.inputs[10].links) == 0:
            return Utils.FloatValue(self.inputs[10].floatValue,self.inputs[10].isDeg)
        
        return self.inputs[10].links[0].from_node.process()
        
    def getMaxTypeValue(self):
        if not self.overrideTypeMaxValue:
            return '_HIDE_'
    
        if len(self.inputs[11].links) == 0:
            return Utils.FloatValue(self.inputs[11].floatValue,self.inputs[11].isDeg)
        
        return self.inputs[11].links[0].from_node.process()
        
    def process(self):
        animType = self.animType.lower()
    
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
        
        if animType == 'HIDE':
            newAnim.Set("memory",'_HIDE_')
            newAnim.Set("axis",'_HIDE_')
            newAnim.Set("begin",'_HIDE_')
            newAnim.Set("end",'_HIDE_')
        
        return newAnim
        
    def inspect(self):
        data = self.process()
        
        print(data.Print())
            
    def presetsettings(self):
        settings = []
        if self.animType != 'TRANSLATION':
            settings.append(["animType",self.animType])
            
        if self.axisType != 'AXIS' and self.animType != 'HIDE':
            settings.append(["axisType",self.axisType])
        return settings
        
    def presetpostsettings(self):
        settings = []
        
        settings.append(["overrideSource",self.overrideSource])
        settings.append(["overrideSourceAddress",self.overrideSourceAddress])
        settings.append(["overrideSelection",self.overrideSelection])
        if self.animType != 'HIDE':
            settings.append(["overrideMemory",self.overrideMemory])
            settings.append(["overrideAxis",self.overrideAxis])
            settings.append(["overrideBegin",self.overrideBegin])
            settings.append(["overrideEnd",self.overrideEnd])
        settings.append(["overrideMinValue",self.overrideMinValue])
        settings.append(["overrideMaxValue",self.overrideMaxValue])
        settings.append(["overrideTypeMinValue",self.overrideTypeMinValue])
        settings.append(["overrideTypeMaxValue",self.overrideTypeMaxValue])
        
        return settings