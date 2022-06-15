from .utility_data import Bone, Skeleton, Model, Animation

##############################
####PRESET DATA GENERATORS####
##############################

# Bones

def BoneGenerator(names,parentBase,makeBaseBone,fieldsize,interval):
    newBoneList = []
    interval.sort()
    
    fieldsize = max(fieldsize,len(str(interval[1])))
    
    for baseName in names.split(","):
        if makeBaseBone == 'YES':
            name = baseName.replace("%","base")
            if name == baseName:
                name += "_base"
            baseBone = Bone(name,parentBase)
            newBoneList.append(baseBone)
            parent = baseBone.name
        else:
            parent = parentBase
        
        for i in range(interval[0],interval[1] + 1):
            idfield = str(i).zfill(fieldsize)
            name = baseName.replace("%",idfield)
            if name == baseName:
                name += "_" + idfield
            newBone = Bone(name,parent)
            newBoneList.append(newBone)
    
    return newBoneList

def BoneStandardWeapon():
    newBoneList = []
    newBoneList.append(Bone("zasleh",""))
    newBoneList.append(Bone("magazine",""))
    newBoneList.append(Bone("selector",""))
    newBoneList.append(Bone("safety",""))
    newBoneList.append(Bone("trigger",""))
    newBoneList.append(Bone("sight",""))
    newBoneList.append(Bone("foresight",""))
    newBoneList.append(Bone("backsight",""))
    newBoneList.append(Bone("bolt",""))
    newBoneList.append(Bone("recoil",""))
    
    return newBoneList
    
def BoneStandardHouse(damCount,doorCount,doorHandles,glassCount):
    newBoneList = []
    
    for i in range(damCount):
        newBoneList.append(Bone("Dam_" + str(i + 1),""))
        newBoneList.append(Bone("Unhide" + str(i + 1),""))
        
    for i in range(doorCount):
        newBoneList.append(Bone("Door_" + str(i + 1),""))
        
        if doorHandles:
            newBoneList.append(Bone("Door_Handle_" + str(i + 1),"Door_" + str(i + 1)))
            newBoneList.append(Bone("Door_Handle_" + str(i + 1) + "_axis","Door_Handle_" + str(i + 1)))
            
    for i in range(glassCount):
        newBoneList.append(Bone("Glass_" + str(i + 1) + "_hide",""))
        newBoneList.append(Bone("Glass_" + str(i + 1) + "_unhide",""))
    
    return newBoneList

def BoneStandardTank(wheelsFix,wheelsDamp):
    newBoneList = []
    
    # Fixed wheels
    for i in range(wheelsFix):
        index = str(i + 1)
        
        newBoneList.append(Bone("koll%".replace("%",index),""))
        newBoneList.append(Bone("kolp%".replace("%",index),""))
        
    # Suspended wheels
    for i in range(wheelsDamp):
        index = str(i + 1)
        
        newBoneList.append(Bone("podkolol%".replace("%",index),""))
        newBoneList.append(Bone("podkolol%_hide".replace("%",index),"podkolol%".replace("%",index)))
        newBoneList.append(Bone("kolol%".replace("%",index),"podkolol%".replace("%",index)))
        newBoneList.append(Bone("podkolop%".replace("%",index),""))
        newBoneList.append(Bone("podkolop%_hide".replace("%",index),"podkolop%".replace("%",index)))
        newBoneList.append(Bone("kolop%".replace("%",index),"podkolop%".replace("%",index)))
        
    return newBoneList

def BoneStandardTurret(identifier,parent):
    newBoneList = []
    
    turretName = "turret"
    gunName = "gun"
    viewName = "gunnerview"
    
    if identifier != "":
        turretName += "_" + identifier
        gunName += "_" + identifier
        viewName += "_" + identifier
        
    recoilName = gunName + "_recoil"
    
    newBoneList.append(Bone(turretName,parent))
    newBoneList.append(Bone(gunName,turretName))
    newBoneList.append(Bone(viewName,gunName))
    newBoneList.append(Bone(recoilName,gunName))
    
    return newBoneList


def BoneReplace(oldList,searchfor,replacewith,result,operation):
    newBoneList = []
    
    for oldBone in oldList:
        oldName = oldBone.name
        newName = oldName.replace(searchfor,replacewith)
        if oldName == newName: # there was nothing to replace
            if result == 'FULL':
                newBoneList.append(oldBone)
        else: # name was changed
            newParent = oldBone.parent.replace(searchfor,replacewith)
            newBone = Bone(newName,newParent)
            
            if result == 'FULL' and operation == 'COPY':
                newBoneList.append(oldBone)
                
            newBoneList.append(newBone)
    
    return newBoneList

def BoneSymmetrize(baseList,stringLeft,stringRight):
    newBoneList = []
    
    for baseBone in baseList:
        newNameLeft = baseBone.name.replace("%",stringLeft)
        newNameRight = baseBone.name.replace("%",stringRight)
        
        if newNameLeft == newNameRight:
            newBoneList.append(baseBone)
            continue
        
        newParentLeft = baseBone.parent.replace("%",stringLeft)
        newParentRight = baseBone.parent.replace("%",stringRight)
        
        newBoneList.append(Bone(newNameLeft,newParentLeft))
        newBoneList.append(Bone(newNameRight,newParentRight))
    
    return newBoneList

# Skeletons

def DefaultSkeleton():
    newSkeleton = Skeleton("Default","")
    return newSkeleton
    
def OFP2_ManSkeleton():
    newSkeleton = Skeleton("OFP2_ManSkeleton","")
    newSkeleton.Set("isDiscrete",False)
    
    # Bones
    
    newSkeleton.AddBone(Bone("Pelvis",""))
    newSkeleton.AddBone(Bone("Spine","Pelvis"))
    newSkeleton.AddBone(Bone("Spine1","Spine"))
    newSkeleton.AddBone(Bone("Spine2","Spine1"))
    newSkeleton.AddBone(Bone("Spine3","Spine2"))
    newSkeleton.AddBone(Bone("Camera","Pelvis"))
    newSkeleton.AddBone(Bone("weapon","Spine1"))
    newSkeleton.AddBone(Bone("launcher","Spine1"))
    
    newSkeleton.AddBone(Bone("neck","Spine3"))
    newSkeleton.AddBone(Bone("neck1","neck"))
    newSkeleton.AddBone(Bone("head","neck1"))
    
    newSkeleton.AddBone(Bone("Face_Hub","head"))
    newSkeleton.AddBone(Bone("Face_Jawbone","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_Jowl","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_chopRight","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_chopLeft","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_LipLowerMiddle","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_LipLowerLeft","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_LipLowerRight","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_Chin","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_Tongue","Face_Jawbone"))
    newSkeleton.AddBone(Bone("Face_CornerRight","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_CheekSideRight","Face_CornerRight"))
    newSkeleton.AddBone(Bone("Face_CornerLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_CheekSideLeft","Face_CornerLeft"))
    newSkeleton.AddBone(Bone("Face_CheekFrontRight","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_CheekFrontLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_CheekUpperRight","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_CheekUpperLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_LipUpperMiddle","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_LipUpperRight","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_LipUpperLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_NostrilRight","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_NostrilLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_Forehead","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_BrowFrontRight","Face_Forehead"))
    newSkeleton.AddBone(Bone("Face_BrowFrontLeft","Face_Forehead"))
    newSkeleton.AddBone(Bone("Face_BrowMiddle","Face_Forehead"))
    newSkeleton.AddBone(Bone("Face_BrowSideRight","Face_Forehead"))
    newSkeleton.AddBone(Bone("Face_BrowSideLeft","Face_Forehead"))
    newSkeleton.AddBone(Bone("Face_Eyelids","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_EyelidUpperRight","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_EyelidUpperLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_EyelidLowerRight","Face_Hub"))
    newSkeleton.AddBone(Bone("Face_EyelidLowerLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("EyeLeft","Face_Hub"))
    newSkeleton.AddBone(Bone("EyeRight","Face_Hub"))
    
    newSkeleton.AddBone(Bone("LeftShoulder","Spine3"))
    newSkeleton.AddBone(Bone("LeftArm","LeftShoulder"))
    newSkeleton.AddBone(Bone("LeftArmRoll","LeftArm"))
    newSkeleton.AddBone(Bone("LeftForeArm","LeftArmRoll"))
    newSkeleton.AddBone(Bone("LeftForeArmRoll","LeftForeArm"))
    newSkeleton.AddBone(Bone("LeftHand","LeftForeArmRoll"))
    newSkeleton.AddBone(Bone("LeftHandRing","LeftHand"))
    newSkeleton.AddBone(Bone("LeftHandRing1","LeftHandRing"))
    newSkeleton.AddBone(Bone("LeftHandRing2","LeftHandRing1"))
    newSkeleton.AddBone(Bone("LeftHandRing3","LeftHandRing2"))
    newSkeleton.AddBone(Bone("LeftHandPinky1","LeftHandRing"))
    newSkeleton.AddBone(Bone("LeftHandPinky2","LeftHandPinky1"))
    newSkeleton.AddBone(Bone("LeftHandPinky3","LeftHandPinky2"))
    newSkeleton.AddBone(Bone("LeftHandMiddle1","LeftHand"))
    newSkeleton.AddBone(Bone("LeftHandMiddle2","LeftHandMiddle1"))
    newSkeleton.AddBone(Bone("LeftHandMiddle3","LeftHandMiddle2"))
    newSkeleton.AddBone(Bone("LeftHandIndex1","LeftHand"))
    newSkeleton.AddBone(Bone("LeftHandIndex2","LeftHandIndex1"))
    newSkeleton.AddBone(Bone("LeftHandIndex3","LeftHandIndex2"))
    newSkeleton.AddBone(Bone("LeftHandThumb1","LeftHand"))
    newSkeleton.AddBone(Bone("LeftHandThumb2","LeftHandThumb1"))
    newSkeleton.AddBone(Bone("LeftHandThumb3","LeftHandThumb2"))
    
    newSkeleton.AddBone(Bone("RightShoulder","Spine3"))
    newSkeleton.AddBone(Bone("RightArm","RightShoulder"))
    newSkeleton.AddBone(Bone("RightArmRoll","RightArm"))
    newSkeleton.AddBone(Bone("RightForeArm","RightArmRoll"))
    newSkeleton.AddBone(Bone("RightForeArmRoll","RightForeArm"))
    newSkeleton.AddBone(Bone("RightHand","RightForeArmRoll"))
    newSkeleton.AddBone(Bone("RightHandRing","RightHand"))
    newSkeleton.AddBone(Bone("RightHandRing1","RightHandRing"))
    newSkeleton.AddBone(Bone("RightHandRing2","RightHandRing1"))
    newSkeleton.AddBone(Bone("RightHandRing3","RightHandRing2"))
    newSkeleton.AddBone(Bone("RightHandPinky1","RightHandRing"))
    newSkeleton.AddBone(Bone("RightHandPinky2","RightHandPinky1"))
    newSkeleton.AddBone(Bone("RightHandPinky3","RightHandPinky2"))
    newSkeleton.AddBone(Bone("RightHandMiddle1","RightHand"))
    newSkeleton.AddBone(Bone("RightHandMiddle2","RightHandMiddle1"))
    newSkeleton.AddBone(Bone("RightHandMiddle3","RightHandMiddle2"))
    newSkeleton.AddBone(Bone("RightHandIndex1","RightHand"))
    newSkeleton.AddBone(Bone("RightHandIndex2","RightHandIndex1"))
    newSkeleton.AddBone(Bone("RightHandIndex3","RightHandIndex2"))
    newSkeleton.AddBone(Bone("RightHandThumb1","RightHand"))
    newSkeleton.AddBone(Bone("RightHandThumb2","RightHandThumb1"))
    newSkeleton.AddBone(Bone("RightHandThumb3","RightHandThumb2"))
    
    newSkeleton.AddBone(Bone("LeftUpLeg","Pelvis"))
    newSkeleton.AddBone(Bone("LeftUpLegRoll","LeftUpLeg"))
    newSkeleton.AddBone(Bone("LeftLeg","LeftUpLegRoll"))
    newSkeleton.AddBone(Bone("LeftLegRoll","LeftLeg"))
    newSkeleton.AddBone(Bone("LeftFoot","LeftLegRoll"))
    newSkeleton.AddBone(Bone("LeftToeBase","LeftFoot"))
    
    newSkeleton.AddBone(Bone("RightUpLeg","Pelvis"))
    newSkeleton.AddBone(Bone("RightUpLegRoll","RightUpLeg"))
    newSkeleton.AddBone(Bone("RightLeg","RightUpLegRoll"))
    newSkeleton.AddBone(Bone("RightLegRoll","RightLeg"))
    newSkeleton.AddBone(Bone("RightFoot","RightLegRoll"))
    newSkeleton.AddBone(Bone("RightToeBase","RightFoot"))
    
    newSkeleton.Set("pivotsModel","A3\\anims_f\data\skeleton\SkeletonPivots.p3d")
    
    return newSkeleton

# Models

def DefaultModel():
    newModel = Model("Default","")
    newModel.Set("animationsList",'_HIDE_')
    return newModel
    
def CloneModel(name,parent):
    newModel = Model(name,parent)
    
    newModel.Set("iscopy",True)
    
    return newModel
    
def ArmaMan(skeletonName,additionalSections = []):
    newModel = Model("ArmaMan","")
    newModel.Set("htMin",60)
    newModel.Set("htMax",1800)
    newModel.Set("afMax",30)
    newModel.Set("mfMax",0)
    newModel.Set("mFact",1)
    newModel.Set("tBody",37)
    
    newModel.AddSection("osobnost")
    newModel.AddSection("Head_Injury")
    newModel.AddSection("Body_Injury")
    newModel.AddSection("l_leg_injury")
    newModel.AddSection("l_arm_injury")
    newModel.AddSection("r_arm_injury")
    newModel.AddSection("r_leg_injury")
    newModel.AddSection("injury_body")
    newModel.AddSection("injury_legs")
    newModel.AddSection("injury_hands")
    newModel.AddSection("clan")
    newModel.AddSection("clan_sign")
    newModel.AddSection("Camo")
    newModel.AddSection("CamoB")
    newModel.AddSection("Camo1")
    newModel.AddSection("Camo2")
    newModel.AddSection("personality")
    newModel.AddSection("hl")
    newModel.AddSection("injury_head")
    newModel.AddSection("insignia")
    newModel.AddSection("ghillie_hide")
    
    for section in additionalSections:
        newModel.AddSection(section)
    
    newModel.Set("skeletonName",skeletonName)
    newModel.Set("animationsList",'_HIDE_')
    
    return newModel

# Animations

def MuzzleflashRot(name,selection,axis):
    newAnim = Animation(name,"rotation","")
    newAnim.Set("source","ammoRandom")
    newAnim.Set("sourceAddress","loop")
    newAnim.Set("selection",selection)
    newAnim.Set("axis",'_HIDE_')
    newAnim.Set("begin",axis[0])
    newAnim.Set("end",axis[1])
    newAnim.Set("typeMaxValue",360 * (3.141592653589793/180))
    return newAnim
    
def TriggerRot(name,selection,axis,angle):
    newAnim = Animation(name,"rotation","")
    newAnim.Set("source","reload")
    newAnim.Set("selection",selection)
    newAnim.Set("axis",axis)
    newAnim.Set("typeMaxValue",angle)
    return newAnim
    
def TriggerMove(name,selection,axis,move):
    newAnim = Animation(name,"translation","")
    newAnim.Set("source","reload")
    newAnim.Set("selection",selection)
    newAnim.Set("axis",axis)
    newAnim.Set("typeMaxValue",move)
    return newAnim
    
def SelectorRot(name,selection,axis,angle):
    newAnim = Animation(name,"rotation","")
    newAnim.Set("source","weaponMode")
    newAnim.Set("selection",selection)
    newAnim.Set("axis",axis)
    newAnim.Set("maxValue",0.25)
    newAnim.Set("typeMaxValue",angle)
    return newAnim

def SightHide(name,selection):
    newAnim = Animation(name,"hide","")
    newAnim.Set("source","hasOptics")
    newAnim.Set("selection",selection)
    newAnim.Set("typeMinValue",0.5)
    newAnim.Set("typeMaxValue",-2)
    newAnim.Set("axis",'_HIDE_')
    newAnim.Set("memory",'_HIDE_')
    newAnim.Set("sourceAddress",'_HIDE_')
    return newAnim
    
def MagazineHide(selection,muzzleindex):
    newAnim = Animation("no_magazine_hide","hide","")
    source = "hasMagazine"
    if muzzleindex > -1:
        source += "." + str(muzzleindex)
    newAnim.Set("source",source)
    newAnim.Set("selection",selection)
    newAnim.Set("typeMinValue",0.5)
    newAnim.Set("typeMaxValue",-1)
    newAnim.Set("axis",'_HIDE_')
    newAnim.Set("memory",'_HIDE_')
    newAnim.Set("sourceAddress",'_HIDE_')
    return newAnim
    
def BulletHide(baseName,muzzleindex,fieldsize,capacity,interval):
    newAnimList = []
    bulletFirst = interval[0]
    bulletLast = interval[1]
    
    source = "revolving"
    if muzzleindex > -1:
        source += "." + str(muzzleindex)
    
    parent = baseName.replace("%","base")
    if parent == baseName:
        parent += "_base"
    
    baseAnim = Animation(parent + "_hide","hide","")
    baseAnim.Set("source",source)
    baseAnim.Set("sourceAddress","mirror")
    baseAnim.Set("selection","empty")
    baseAnim.Set("memory",'_HIDE_')
    baseAnim.Set("axis",'_HIDE_')
    baseAnim.Set("minValue",-1)
    baseAnim.Set("maxValue",0)
    baseAnim.Set("typeMinValue",0)
    baseAnim.Set("typeMaxValue",'_HIDE_')
    
    newAnimList.append(baseAnim)
    fieldsize = max(fieldsize,len(str(capacity)))
    
    for i in range(bulletFirst,bulletLast + 1):
        idfield = str(i).zfill(fieldsize)
        name = baseName.replace("%",idfield)
        if name == baseName:
            name += "_" + idfield
        newAnim = Animation(name + "_hide","hide",parent + "_hide")
        newAnim.Set("source",'_HIDE_')
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection",name)
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("axis",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        hideValue = (((i-0.5)/capacity))
        newAnim.Set("typeMinValue",round(hideValue,6))
        newAnim.Set("typeMaxValue",'_HIDE_')
        
        newAnimList.append(newAnim)
    
    return newAnimList
    
def DoorRot(doorRange,handle,angleDoor,angleHandle):
    newAnimList = []
    
    baseAnim = Animation("Door_base_rot","rotation","")
    baseAnim.Set("source","empty")
    baseAnim.Set("selection","empty")
    baseAnim.Set("axis","empty")
    baseAnim.Set("typeMaxValue",angleDoor)
    
    if handle:
        baseAnim.Set("minValue",0.1)
    
    newAnimList.append(baseAnim)
    
    for i in range(doorRange[0], doorRange[1] + 1):
        index = str(i)
    
        newDoorAnim = Animation("Door_%_rot".replace("%",index),"rotation","Door_base_rot")
        newDoorAnim.Set("source","Door_%_source".replace("%",index))
        newDoorAnim.Set("sourceAddress",'_HIDE_')
        newDoorAnim.Set("selection","Door_%".replace("%",index))
        newDoorAnim.Set("axis","Door_%_axis".replace("%",index))
        newDoorAnim.Set("memory",'_HIDE_')
        newDoorAnim.Set("minValue",'_HIDE_')
        newDoorAnim.Set("maxValue",'_HIDE_')
        newDoorAnim.Set("typeMinValue",'_HIDE_')
        newDoorAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newDoorAnim)
        
        if handle:
            newHandleAnim1 = Animation("Door_Handle_%_rot_1".replace("%",index),"rotation","")
            newHandleAnim1.Set("source","Door_%_source".replace("%",index))
            newHandleAnim1.Set("selection","Door_Handle_%".replace("%",index))
            newHandleAnim1.Set("axis","Door_Handle_%_axis".replace("%",index))
            newHandleAnim1.Set("maxValue",0.1)
            newHandleAnim1.Set("typeMaxValue",angleHandle)
            
            newHandleAnim2 = Animation("Door_Handle_%_rot_2".replace("%",index),"rotation","Door_Handle_%_rot_1".replace("%",index))
            newHandleAnim2.Set("source",'_HIDE_')
            newHandleAnim2.Set("sourceAddress",'_HIDE_')
            newHandleAnim2.Set("selection",'_HIDE_')
            newHandleAnim2.Set("axis",'_HIDE_')
            newHandleAnim2.Set("memory",'_HIDE_')
            newHandleAnim2.Set("minValue",0.1)
            newHandleAnim2.Set("minValue",0.4)
            newHandleAnim2.Set("typeMinValue",'_HIDE_')
            newHandleAnim2.Set("typeMaxValue",-angleHandle)
            
            newAnimList.append(newHandleAnim1)
            newAnimList.append(newHandleAnim2)
            
    
    return newAnimList

def DoorMove(doorRange,offsetDoor):
    newAnimList = []
    
    baseAnim = Animation("Door_base_move","translation","")
    baseAnim.Set("source","empty")
    baseAnim.Set("selection","empty")
    baseAnim.Set("axis","empty")
    baseAnim.Set("typeMaxValue",offsetDoor)
    newAnimList.append(baseAnim)
    
    for i in range(doorRange[0],doorRange[1] + 1):
        index = str(i)
        
        newDoorAnim = Animation("Door_%_move".replace("%",index),"translation","Door_base_move")
        newDoorAnim.Set("source","Door_%_source".replace("%",index))
        newDoorAnim.Set("sourceAddress",'_HIDE_')
        newDoorAnim.Set("selection","Door_%".replace("%",index))
        newDoorAnim.Set("axis","Door_%_axis".replace("%",index))
        newDoorAnim.Set("memory",'_HIDE_')
        newDoorAnim.Set("minValue",'_HIDE_')
        newDoorAnim.Set("maxValue",'_HIDE_')
        newDoorAnim.Set("typeMinValue",'_HIDE_')
        newDoorAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newDoorAnim)
    
    return newAnimList


def GlassHide(glassCount):
    newAnimList = []
    
    for i in range(glassCount):
        index = str(i + 1)
        
        newAnim1 = Animation("Glass_%_hide".replace("%",index),"hide","")
        newAnim1.Set("source","Glass_%_source".replace("%",index))
        newAnim1.Set("sourceAddress",'_HIDE_')
        newAnim1.Set("selection","Glass_%_hide".replace("%",index))
        newAnim1.Set("memory",'_HIDE_')
        newAnim1.Set("axis",'_HIDE_')
        newAnim1.Set("typeMinValue",0.99999)
        newAnim1.Set("typeMaxValue",'_HIDE_')
        
        newAnim2 = Animation("Glass_%_unhide".replace("%",index),"hide","Glass_%_hide".replace("%",index))
        newAnim2.Set("source",'_HIDE_')
        newAnim2.Set("sourceAddress",'_HIDE_')
        newAnim2.Set("selection","Glass_%_unhide".replace("%",index))
        newAnim2.Set("memory",'_HIDE_')
        newAnim2.Set("axis",'_HIDE_')
        newAnim2.Set("minValue",'_HIDE_')
        newAnim2.Set("maxValue",'_HIDE_')
        newAnim2.Set("typeMinValue",0)
        newAnim2.Set("typeMaxValue",0.99999)
        
        newAnimList.append(newAnim1)
        newAnimList.append(newAnim2)
    
    return newAnimList
    
def TankWheels(wheelsFix,wheelsDamp,damping):
    newAnimList = []
    
    
    baseAnim = Animation("wheel_base_rot","rotationX","")
    baseAnim.Set("source","empty")
    baseAnim.Set("sourceAddress","loop")
    baseAnim.Set("selection","empty")
    baseAnim.Set("axis","empty")
    baseAnim.Set("typeMaxValue",-360 * (3.141592653589793/180))
    newAnimList.append(baseAnim)
    
    for i in range(wheelsFix):
        index = str(i + 1)
        
        newAnim = Animation("wheel_koll%".replace("%",index),"rotationX","wheel_base_rot")
        newAnim.Set("source","wheell")
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","koll%".replace("%",index))
        newAnim.Set("axis","wheel_1_%_axis".replace("%",index))
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
        newAnim = Animation("wheel_kolp%".replace("%",index),"rotationX","wheel_base_rot")
        newAnim.Set("source","wheelr")
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","kolp%".replace("%",index))
        newAnim.Set("axis","wheel_2_%_axis".replace("%",index))
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
    if wheelsDamp > 0:
        newAnim = Animation("wheel_base_damp","translation","")
        newAnim.Set("source","damper")
        newAnim.Set("selection","empty")
        newAnim.Set("axis","damper_axis")
        newAnim.Set("typeMinValue",damping[0])
        newAnim.Set("typeMaxValue",damping[1])
        newAnimList.append(newAnim)
        
        newAnim = Animation("wheel_hide_damage","hide","")
        newAnim.Set("source","damage")
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","empty")
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("axis",'_HIDE_')
        newAnim.Set("typeMinValue",1)
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
    for i in range(wheelsDamp):
        index = str(i + 1)
        axisindex = str(wheelsFix + i + 1)
        
        # Wheel rotations
        newAnim = Animation("wheel_kolol%".replace("%",index),"rotationX","wheel_base_rot")
        newAnim.Set("source","wheell")
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","kolol%".replace("%",index))
        newAnim.Set("axis","wheel_1_%_axis".replace("%",axisindex))
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
        newAnim = Animation("wheel_kolop%".replace("%",index),"rotationX","wheel_base_rot")
        newAnim.Set("source","wheelr")
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","kolop%".replace("%",index))
        newAnim.Set("axis","wheel_2_%_axis".replace("%",axisindex))
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
        # Wheel damping
        newAnim = Animation("wheel_podkolol%".replace("%",index),"translation","wheel_base_damp")
        newAnim.Set("source",'_HIDE_')
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","podkolol%".replace("%",index))
        newAnim.Set("axis",'_HIDE_')
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
        newAnim = Animation("wheel_podkolop%".replace("%",index),"translation","wheel_base_damp")
        newAnim.Set("source",'_HIDE_')
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","podkolop%".replace("%",index))
        newAnim.Set("axis",'_HIDE_')
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
        # Damage hiding
        newAnim = Animation("podkolol%_hide_damage".replace("%",index),"hide","wheel_hide_damage")
        newAnim.Set("source",'_HIDE_')
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","podkolol%_hide".replace("%",index))
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("axis",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
        newAnim = Animation("podkolop%_hide_damage".replace("%",index),"hide","wheel_hide_damage")
        newAnim.Set("source",'_HIDE_')
        newAnim.Set("sourceAddress",'_HIDE_')
        newAnim.Set("selection","podkolop%_hide".replace("%",index))
        newAnim.Set("memory",'_HIDE_')
        newAnim.Set("axis",'_HIDE_')
        newAnim.Set("minValue",'_HIDE_')
        newAnim.Set("maxValue",'_HIDE_')
        newAnim.Set("typeMinValue",'_HIDE_')
        newAnim.Set("typeMaxValue",'_HIDE_')
        newAnimList.append(newAnim)
        
    return newAnimList

def TurretRot(identifier,isMain,recoilOffset):
    newAnimList = []
    
    # Turret rotation
    nameTurretRot = "mainturret"
    selectionTurret = "turret"
    if identifier != "":
        selectionTurret += "_" + identifier
        
    if not isMain:
        nameTurretRot = selectionTurret + "_rot"
        
    turretRot = Animation(nameTurretRot,"rotation","")
    turretRot.Set("source",nameTurretRot)
    turretRot.Set("sourceAddress",'_HIDE_')
    turretRot.Set("selection",selectionTurret)
    turretRot.Set("axis",selectionTurret + "_axis")
    turretRot.Set("minValue",-360 * (3.141592653589793/180))
    turretRot.Set("maxValue",360 * (3.141592653589793/180))
    turretRot.Set("typeMinValue",-360 * (3.141592653589793/180))
    turretRot.Set("typeMaxValue",360 * (3.141592653589793/180))
    
    newAnimList.append(turretRot)
    
    # Gun elevation
    nameGunRot = "maingun"
    selectionGun = "gun"
    if identifier != "":
        selectionGun += "_" + identifier
        
    if not isMain:
        nameGunRot = selectionGun + "_rot"
        
    gunRot = Animation(nameGunRot,"rotation",nameTurretRot)
    gunRot.Set("source",nameGunRot)
    gunRot.Set("sourceAddress",'_HIDE_')
    gunRot.Set("selection",selectionGun)
    gunRot.Set("memory",'_HIDE_')
    gunRot.Set("axis",selectionGun + "_axis")
    gunRot.Set("minValue",'_HIDE_')
    gunRot.Set("maxValue",'_HIDE_')
    gunRot.Set("typeMinValue",'_HIDE_')
    gunRot.Set("typeMaxValue",'_HIDE_')
    
    newAnimList.append(gunRot)
    
    if recoilOffset == 0:
        return newAnimList
        
    # Gun recoil
    selectionRecoil = selectionGun + "_recoil"
    
    recoilMove = Animation(selectionRecoil,"translation","")
    recoilMove.Set("source",selectionRecoil + "_source")
    recoilMove.Set("selection",selectionRecoil)
    recoilMove.Set("axis",selectionRecoil + "_axis")
    recoilMove.Set("minValue",0.5)
    recoilMove.Set("typeMaxValue",recoilOffset)
    
    newAnimList.append(recoilMove)
    
    
    return newAnimList