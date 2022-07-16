from .utility_print import ConfigFormatter

#############################
####EXPORT DATA STRUCTURE####
#############################

# Validate name string
def ValidName(string,allowSpace = False,allowEmpty = False,allowPeriod = False):
    isValid = True
    
    if allowEmpty and string == "":
        return True
    elif not allowEmpty and string == "":
        return False
    
    if string[0].isdigit() or string[0] == "_" or string[len(string)-1] == "_":
        isValid = False
    else:
        for char in string:
            if not ((char.isalnum() or char == "_" or char == ".") or (allowSpace and char == " ") or (allowPeriod and char == ".")):
                isValid = False
                break
    return isValid

# Info storing class to contain validation info
class ValidationInfo:
    # Class variables
    infoList = []
    errors = 0
    warnings = 0
    
    # Constructor
    def __init__(self):
        self.infoList = []
        self.errors = 0
        self.warnings = 0
        
    # Operator functions
    def NewErr(self,source,info):
        self.errors += 1
        self.infoList.append([2,source,info])
    
    def NewWarn(self,source,info):
        self.warnings += 1
        self.infoList.append([1,source,info])
        
    def NewInfo(self,source,info):
        self.infoList.append([0,source,info])
        
    def CountErr(self):
        return self.errors
        
    def CountWarn(self):
        return self.warnings
        
    def Evaluate(self,warnsAreErrs = True):
        validData = True
        errCount = self.CountErr()
        if warnsAreErrs:
            errCount += self.CountWarn()
       
        if errCount > 0:
            validData = False
        
        return validData
    
    # Data printer
    def Print(self,dumpAll = False):
        printOutput = ""
        
        printOutput += "Number of warnings   : " + str(self.CountWarn()) + ConfigFormatter.Endl()
        printOutput += "Number of errors     : " + str(self.CountErr()) + ConfigFormatter.Endl()
        printOutput += ConfigFormatter.Endl()
        
        maxLength = 0
        for entry in self.infoList:
            if len(entry[1]) > maxLength:
                maxLength = len(entry[1])
                
        maxLength += 4
            
        for entry in self.infoList:
            infoType = "info"
            if entry[0] == 2:
                infoType = "error"
            elif entry[0] == 1:
                infoType = "warning"
                
            infoType = infoType.upper()
            infoType += (" " * (11-len(infoType)))
            
            infoSubject = "(" + entry[1] + ")"
            infoSubject += (" " * (maxLength - len(entry[1])))
            
            printOutput += (infoType + infoSubject + ": " + entry[2] + ConfigFormatter.Endl())
            
        return printOutput

# Base class for data strucutre
class ClassBase:
    # Class variables
    name = ""
    parent = ""
    iscopy = False
    
    # Constructor
    def __init__(self,selfName,parentName = ""):
        self.name = selfName
        self.parent = parentName
        self.iscopy = False
    
    # String representation
    def __repr__(self):
        parentOut = ""
        if self.parent != "":
            parentOut = (": " + self.parent)
        return ("class " + self.name + parentOut)
    
    # Generic setter
    def Set(self,propertyName,value):
        if not hasattr(self,propertyName):
            return 0
            
        setattr(self,propertyName,value)
        return -1
    
    # Generic getter
    def Get(self,propertyName):
        if not hasattr(self,propertyName):
            return 0
            
        return getattr(self,propertyName)
    
    # Data printer (not implemented here)
    def Print(self,tabs = 0):
        return " // print function is not defined for this class"
    
    # Data validator (not implemented here)
    def Validate(self,validator,optional = ""):
        # DO VALIDATION ALGORITHMS
        # NOT IMPLEMENTED HERE
        return validator

class Bone(ClassBase):
    # Class variables
    name = ""
    parent = ""
    
    # Constructor
    def __init__(self,boneName,parentName = ""):
        self.name = boneName
        self.parent = parentName
    
    # String representation
    def __repr__(self):
        return ("\"" + self.name + "\", \"" + self.parent + "\"")
    
    # Type comparer
    def __eq__(self,other):
        if not isinstance(other,Bone):
            return False
        
        if self.name != other.name:
            return False
            
        return True
    
    # Data validator
    def Validate(self,validator,skeletonname):
        
        entryOwner = "CfgSkeletons >> " + skeletonname + " >> skeletonBones >> "+ self.name
        
        if not ValidName(self.name):
            validator.NewErr(self.name,"invalid bone name (" + self.name + ")")
        
        return validator

class Skeleton(ClassBase):
    # Class variables
    isDiscrete = True
    skeletonInherit = ""
    skeletonBones = []
    pivotsModel = '_HIDE_'
    
    # Constructor
    def __init__(self,selfName,parentName = ""):
        self.name = selfName
        self.parent = parentName
        self.skeletonBones = []
        self.pivotsModel = '_HIDE_'
        self.iscopy = False
    
    # Type comparer
    def __eq__(self,other):
        if not isinstance(other,Skeleton):
            return False
            
        if self.name != other.name:
            return False
            
        return True
    
    # Operator functions
    def AddBone(self,boneItem):
        self.skeletonBones.append(boneItem)
    
    # Data printer
    def Print(self,tabs = 0):
        printOutput = ""
        
        printOutput += ConfigFormatter.ClassOpen(self.name,self.parent,tabs)
        
        # Print nothing but the class name and parent if it's just an intended copy
        if self.iscopy:
            printOutput += ConfigFormatter.ClassClose() + ConfigFormatter.Endl()
            return printOutput
        else:
            printOutput += ConfigFormatter.Endl()
        
        omitedProps = 0
        
        if self.isDiscrete != '_HIDE_':
            printOutput += ConfigFormatter.Property("isDiscrete",self.isDiscrete,True,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
            
        if self.skeletonInherit != '_HIDE_':
            printOutput += ConfigFormatter.Property("skeletonInherit",self.skeletonInherit,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
            
        if self.skeletonBones != '_HIDE_':
            bonePrintList = []
            for bone in self.skeletonBones:
                bonePrintList.append(bone.Get("name"))
                bonePrintList.append(bone.Get("parent"))
            
            printOutput += ConfigFormatter.Property("skeletonBones",bonePrintList,[""],tabs + 1,False,2) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.pivotsModel != '_HIDE_':
            printOutput += ConfigFormatter.Property("pivotsModel",self.pivotsModel,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if omitedProps == 4:
            printOutput += ConfigFormatter.Comment("this class does not have any own properties, it may be best to remove it",tabs + 1) + ConfigFormatter.Endl()
        
        printOutput += ConfigFormatter.ClassClose(tabs) + ConfigFormatter.Endl()
        
        return printOutput
        
    # Data validator
    def Validate(self,validator):
        
        entryOwner = "CfgSkeletons >> " + self.name
        
        # validate name
        if not ValidName(self.name):
            validator.NewErr(entryOwner,"invalid class name (" + self.name + ")")
            
        # validate bones
        if self.skeletonBones != '_HIDE_':
            entryOwner += " >> skeletonBones"
                
            checklist = []
            for bone in self.skeletonBones:
                if bone.name not in checklist and (bone.parent == "" or bone.parent in checklist):
                    checklist.append(bone.name)
                
            # validate duplicates
            if len(self.skeletonBones) != len(set(checklist)):
                validator.NewErr(entryOwner,"bone names are not unique or parents are missing and so bones cannot be further validated")
                return validator # escape
                    
            if len(checklist) != len(self.skeletonBones):
                validator.NewErr(entryOwner,"bone order does not support the parenting structure so bones cannot be further validated")
                return validator # escape
                
            # validate each bone
            for bone in self.skeletonBones:
                validator = bone.Validate(validator,self.name)
        
        return validator

class Animation(ClassBase):
    # Class variables
    animType = "translation"
    source = ""
    sourceAddress = "clamp"
    selection = ""
    memory = True
    axis = ""
    begin = '_HIDE_'
    end = '_HIDE_'
    minValue = 0
    maxValue = 1
    typeMinValue = 0
    typeMaxValue = 1
    
    # Constructor
    def __init__(self,selfName,selftype = "translation",parentName = ""):
        self.name = selfName
        self.parent = parentName
        self.animType = selftype
        self.iscopy = False
        
        if selftype == "hide":
            self.memory = '_HIDE_'
            self.axis = '_HIDE_'
            self.typeMaxValue = '_HIDE_'
    
    # Type comparer
    def __eq__(self,other):
        if not isinstance(other,Animation):
            return False
            
        if self.name != other.name:
            return False
            
        return True
    
    # Data printer
    def Print(self,tabs = 0):
        printOutput = ""
        printOutput += ConfigFormatter.ClassOpen(self.name,self.parent,tabs)
        
        # Print nothing but the class name and parent if it's just an intended copy
        if self.iscopy:
            printOutput += ConfigFormatter.ClassClose() + ConfigFormatter.Endl()
            return printOutput
        else:
            printOutput += ConfigFormatter.Endl()
        
        omitedProps = 0
        
        if self.animType != '_HIDE_' and self.parent == "":
            printOutput += ConfigFormatter.Property("type",self.animType,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.source != '_HIDE_':
            printOutput += ConfigFormatter.Property("source",self.source,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.sourceAddress != '_HIDE_':
            printOutput += ConfigFormatter.Property("sourceAddress",self.sourceAddress,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.selection != '_HIDE_':
            printOutput += ConfigFormatter.Property("selection",self.selection,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.memory != '_HIDE_':
            printOutput += ConfigFormatter.Property("memory",int(self.memory),0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.axis != '_HIDE_':
            printOutput += ConfigFormatter.Property("axis",self.axis,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.begin != '_HIDE_':
            printOutput += ConfigFormatter.Property("begin",self.begin,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.end != '_HIDE_':
            printOutput += ConfigFormatter.Property("end",self.end,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.minValue != '_HIDE_':
            printOutput += ConfigFormatter.Property("minValue",self.minValue,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.maxValue != '_HIDE_':
            printOutput += ConfigFormatter.Property("maxValue",self.maxValue,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.typeMinValue != '_HIDE_':
            propName = "offset0"
            
            if self.animType in ["rotation","rotationX","rotationY","rotationZ"]:
                propName = "angle0"
            elif self.animType == "hide":
                propName = "hideValue"
            
            printOutput += ConfigFormatter.Property(propName,self.typeMinValue,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.typeMaxValue != '_HIDE_':
            propName = "offset1"
            
            if self.animType in ["rotation","rotationX","rotationY","rotationZ"]:
                propName = "angle1"
            elif self.animType == "hide":
                propName = "unHideValue"
            
            printOutput += ConfigFormatter.Property(propName,self.typeMaxValue,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if omitedProps == 12:
            printOutput += ConfigFormatter.Comment("this class does not have any own properties, it may be best to remove it",tabs + 1) + ConfigFormatter.Endl()
        
        printOutput += ConfigFormatter.ClassClose(tabs) + ConfigFormatter.Endl()
        
        return printOutput

    # Data validator
    def Validate(self,validator,modelname):
        
        entryOwner = "CfgModels >> " + modelname + " >> " + self.name
        
        # validate name
        if not ValidName(self.name):
            validator.NewErr(entryOwner,"invalid class name (" + self.name + ")")
        
        # validate source name
        if self.source != '_HIDE_':
            if self.source == "":
                validator.NewWarn(entryOwner,"source is not defined so there is nothing to drive the animation")
            
            if not ValidName(self.source,False,True,True):
                validator.NewWarn(entryOwner,"source name is invalid")
        
        # validate selection name
        if self.selection != '_HIDE_':
            if self.selection == "":
                validator.NewWarn(entryOwner,"selection is not defined so there is nothing to animate")
            
            if not ValidName(self.selection,False,True,True):
                validator.NewWarn(entryOwner,"selection name is invalid")
        
        # validate axis name
        # TO DO LATER
        
        return validator

class Animations(ClassBase):
    # Class variables
    animList = []
    
    # Constructor
    def __init__(self,inherit = False):
        self.name = "Animations"
        self.animList = []
        if inherit:
            self.parent = "Animations"
    
    # Operator functions
    def AddAnim(self,newAnim):
        self.animList.append(newAnim)
    
    # Data printer
    def Print(self,tabs = 0):
        printOutput = ""
        printOutput += ConfigFormatter.ClassOpen(self.name,self.parent,tabs) + ConfigFormatter.Endl()
        
        if len(self.animList) == 0:
            printOutput += ConfigFormatter.Comment("there are no animations" + ConfigFormatter.Endl(),tabs + 1)
        else:
            for anim in self.animList:
                printOutput += anim.Print(tabs + 1)
        
        printOutput += ConfigFormatter.ClassClose(tabs) + ConfigFormatter.Endl()
        
        return printOutput
        
    # Data validator
    def Validate(self,validator,modelname):
        entryOwner = "CfgModels >> " + modelname + " >> Animations"
        
        # validate parenting order
        checklist = []
        for anim in self.animList:
            if anim.name not in checklist and (anim.parent == "" or anim.parent in checklist):
                checklist.append(anim.name)
            
        # validate duplicates
        if len(self.animList) != len(set(checklist)):
            validator.NewErr(entryOwner,"animation class names are not unique or parents are missing so animations cannot be further validated")
            return validator # escape
                
        if len(checklist) != len(self.animList):
            validator.NewErr(entryOwner,"animation class order does not support the parenting structure so animations cannot be further validated")
            return validator # escape
            
        # validate each skeleton
        for anim in self.animList:
            validator = anim.Validate(validator,modelname)
        
        return validator

class Model(ClassBase):
    # Class variables
    skeletonName = ""
    sectionsInherit = ""
    sections = []
    animationsList = Animations()
    htMin = '_HIDE_'
    htMax = '_HIDE_'
    afMax = '_HIDE_'
    mfMax = '_HIDE_'
    mFact = '_HIDE_'
    tBody = '_HIDE_'
    
    # Constructor
    def __init__(self,selfName,parentName = "",inheritAnims = False):
        self.name = selfName
        self.parent = parentName
        self.sections = []
        self.animationsList = Animations(inheritAnims)
        self.htMin = '_HIDE_'
        self.htMax = '_HIDE_'
        self.afMax = '_HIDE_'
        self.mfMax = '_HIDE_'
        self.mFact = '_HIDE_'
        self.tBody = '_HIDE_'
        self.iscopy = False
    
    # Type comparer
    def __eq__(self,other):
        if not isinstance(other,Model):
            return False
            
        if self.name != other.name:
            return False
            
        return True
    
    # Operator functions
    def AddAnim(self,newAnim):
        self.animationsList.AddAnim(newAnim)
        
    def AddSection(self,newSection):
        self.sections.append(newSection)
    
    # Data printer
    def Print(self,tabs = 0):
        printOutput = ""
        
        printOutput += ConfigFormatter.ClassOpen(self.name,self.parent,tabs)
        
        # Print nothing but the class name and parent if it's just an intended copy
        if self.iscopy:
            printOutput += ConfigFormatter.ClassClose() + ConfigFormatter.Endl()
            return printOutput
        else:
            printOutput += ConfigFormatter.Endl()
        
        omitedProps = 0
        
        if self.skeletonName != '_HIDE_':
            printOutput += ConfigFormatter.Property("skeletonName",self.skeletonName,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.htMin != '_HIDE_':
            printOutput += ConfigFormatter.Property("htMin",self.htMin,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.htMax != '_HIDE_':
            printOutput += ConfigFormatter.Property("htMax",self.htMax,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.afMax != '_HIDE_':
            printOutput += ConfigFormatter.Property("afMax",self.afMax,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.mfMax != '_HIDE_':
            printOutput += ConfigFormatter.Property("mfMax",self.mfMax,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.mFact != '_HIDE_':
            printOutput += ConfigFormatter.Property("mFact",self.mFact,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.tBody != '_HIDE_':
            printOutput += ConfigFormatter.Property("tBody",self.tBody,0,tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.sectionsInherit != '_HIDE_':
            printOutput += ConfigFormatter.Property("sectionsInherit",self.sectionsInherit,"",tabs + 1) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.sections != '_HIDE_':
            printOutput += ConfigFormatter.Property("sections",self.sections,[""],tabs + 1,False) + ConfigFormatter.Endl()
        else:
            omitedProps += 1
        
        if self.animationsList != '_HIDE_':
            printOutput += self.animationsList.Print(tabs + 1)
        else:
            omitedProps += 1
            
        
        if omitedProps == 9:
            printOutput += ConfigFormatter.Comment("this class does not have any own properties, it may be best to remove it",tabs + 1) + ConfigFormatter.Endl()
        
        printOutput += ConfigFormatter.ClassClose(tabs) + ConfigFormatter.Endl()
        
        return printOutput
        
    # Data validator
    def Validate(self,validator):
    
        entryOwner = "CfgModels >> " + self.name
        
        # validate name
        if not ValidName(self.name):
            validator.NewErr(entryOwner,"invalid class name (" + self.name + ")")
            
        # validate sections
        entryOwner += " >> sections"
        if self.sections != '_HIDE_':
            for section in self.sections:
                if self.sections.count(section) > 1:
                    validator.NewWarn(entryOwner,"duplicate sections")
                    break
                
        # validate animations
        if self.animationsList != '_HIDE_':
            validator = self.animationsList.Validate(validator,self.name)
        
        return validator

class CfgSkeletons(ClassBase):
    # Class variables
    skeletonList = []
    
    # Constructor
    def __init__(self):
        self.name = "CfgSkeletons"
        self.parent = ""
        self.skeletonList = []
    
    # Operator functions
    def AddSkeleton(self,newSkeleton):
        self.skeletonList.append(newSkeleton)
    
    # Data printer
    def Print(self,tabs = 0):
        printOutput = ""
        printOutput += ConfigFormatter.ClassOpen(self.name,self.parent,tabs) + ConfigFormatter.Endl()
        
        if len(self.skeletonList) == 0:
            printOutput += ConfigFormatter.Comment("there are no skeletons" + ConfigFormatter.Endl(),tabs + 1)
        else:
            for skelly in self.skeletonList:
                printOutput += skelly.Print(tabs + 1)
        
        printOutput += ConfigFormatter.ClassClose(tabs) + ConfigFormatter.Endl()
        
        return printOutput
    
    # Data validator
    def Unique(self):
    
        for skelly in self.skeletonList:
            if self.skeletonList.count(skelly) > 1:
                return False
        
        return True
        
    def SortParenting(self):
        success = True
        sortedList = []
        
        # sorting iteration
        for i in range(len(self.skeletonList)):
            # independent classes
            for skelly in self.skeletonList:
                if skelly not in sortedList and (skelly.parent == "" or Skeleton(skelly.parent,"") in sortedList):
                    sortedList.append(skelly)
        
        if len(sortedList) != len(self.skeletonList):
            success = False
        else:
            self.skeletonList = sortedList
        
        return success
        
    def Validate(self,validator):
        
        # validate parenting order
        checklist = []
        for skelly in self.skeletonList:
            if skelly.name not in checklist and (skelly.parent == "" or skelly.parent in checklist):
                checklist.append(skelly.name)
            
        # validate duplicates
        if len(self.skeletonList) != len(set(checklist)):
            validator.NewErr("CfgSkeletons","class names are not unique so skeletons cannot be further validated")
            return validator # escape
                
        if len(checklist) != len(self.skeletonList):
            validator.NewErr("CfgSkeletons","class order does not support the parenting structure so skeletons cannot be further validated")
            return validator # escape
            
        # validate each skeleton
        for skelly in self.skeletonList:
            validator = skelly.Validate(validator)
            
        return validator

class CfgModels(ClassBase):
    # Class variables
    modelList = []
    
    # Constructor
    def __init__(self):
        self.name = "CfgModels"
        self.parent = ""
        self.modelList = []
        
    # Operator functions
    def AddModel(self,newModel):
        self.modelList.append(newModel)
        
    # Data printer
    def Print(self,tabs = 0):
        printOutput = ""
        printOutput += ConfigFormatter.ClassOpen(self.name,self.parent,tabs) + ConfigFormatter.Endl()
        
        if len(self.modelList) == 0:
            printOutput += ConfigFormatter.Comment("there are no models" + ConfigFormatter.Endl(),tabs + 1)
        else:
            for mesh in self.modelList:
                printOutput += mesh.Print(tabs + 1)
        
        printOutput += ConfigFormatter.ClassClose(tabs) + ConfigFormatter.Endl()
        
        return printOutput
    
    # Data validator
    def Unique(self):
        
        for mesh in self.modelList:
            if self.modelList.count(mesh) > 1:
                return False
        
        return True
        
    def SortParenting(self):
        success = True
        sortedList = []
        
        # sorting iteration
        for i in range(len(self.modelList)):
            # independent classes
            for mesh in self.modelList:
                if mesh not in sortedList and (mesh.parent == "" or Model(mesh.parent,"") in sortedList):
                    sortedList.append(mesh)
        
        if len(sortedList) != len(self.modelList):
            success = False
        else:
            self.modelList = sortedList
        
        return success
        
    def Validate(self,validator):
        
        # validate parenting order
        checklist = []
        for mesh in self.modelList:
            if mesh.name not in checklist and (mesh.parent == "" or mesh.parent in checklist):
                checklist.append(mesh.name)
            
        # validate duplicates
        if len(self.modelList) != len(set(checklist)):
            validator.NewErr("CfgModels","class names are not unique so models cannot be further validated")
            return validator # escape
                
        if len(checklist) != len(self.modelList):
            validator.NewErr("CfgModels","class order does not support the parenting structure so models cannot be further validated")
            return validator # escape
            
        # validate each skeleton
        for mesh in self.modelList:
            validator = mesh.Validate(validator)
            
        return validator

#############################
####IMPORT DATA STRUCTURE####
#############################

class ImportClass:
    # Class variables
    name = ""
    parent = ""
    elements = []
    
    # Constructor
    def __init__(self,classname,classparent):
        self.name = classname
        self.parent = classparent
        self.elements = []
   
    # String representation
    def __repr__(self):
        parentOut = ""
        if self.parent != "":
            parentOut = (": " + self.parent)
        return ("class " + self.name + parentOut)
        
    def AddElement(self,name,value):
        self.elements.append(name)
        setattr(self,name,value)