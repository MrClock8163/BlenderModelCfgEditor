import os
import sys
import importlib
import bpy
from . import utility

###############################
####PRESET SETUP GENERATORS####
###############################

def AddSetup(self,context,presettag):
    
    node_tree = context.space_data.node_tree
    
    presetdict = None
    for preset in GetSetupDefinitions():
        if preset.get("tag") == presettag:
            presetdict = preset
    
    if presetdict is None:
        utility.ShowInfoBox("Preset not found","Error",'ERROR')
        return
    
    # create nodes and set locations
    newNodeList = []
    for i in range(len(presetdict.get("nodes"))):
        newNode = node_tree.nodes.new(presetdict.get("nodes")[i])
        newNode.location = [presetdict.get("x")[i],presetdict.get("y")[i]]
        newNodeList.append(newNode)
    
    if len(newNodeList) == 0:
        return
    
    # process settings before trying to create links (important for list type nodes)
    for setting in presetdict.get("settings"):
        setattr(newNodeList[setting[0]],setting[1],setting[2])
    
    # create links
    for link in presetdict.get("links"):
        node_tree.links.new(newNodeList[link[0]].outputs[link[2]],newNodeList[link[1]].inputs[link[3]])
    return

# Enum property items function
def GetSetups(self,context):
    items = []
    
    for dicty in GetSetupDefinitions():
        items.append((dicty.get("tag"),dicty.get("name"),dicty.get("desc")))
    
    return items

# Get setup presets both built-in and custom
def GetSetupDefinitions():
    returnpresets = []
    
    addonPrefs = bpy.context.preferences.addons[__package__].preferences
    dir_custom = addonPrefs.customSetupPresets
    
    returnpresets += presets
    returnpresets += GetSetupsFromDir(dir_custom)
    
    return returnpresets

# Read custom presetes from external files
def GetSetupsFromDir(folder):
    files = []
    
    if not os.path.isdir(folder):
        return []
    
    for item in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,item)):
            if os.path.splitext(item)[1] == ".py":
                files.append(item)
    
    sys.path.append(folder)
    returnpresets = []
    for file in files:
        module = importlib.import_module(file.split(".")[0])
        returnpresets.append(module.preset)
    
    return returnpresets
    
# Preset dictionaries
generic = {
    "tag" : 'GENERIC',
    "name" : "Generic",
    "desc" : "Skeleton, bones list, model, sections list",
    "nodes" : ["MCFG_N_Skeleton","MCFG_N_Model","MCFG_N_BoneList","MCFG_N_Bone","MCFG_N_SectionList"],
    "x" : [0,300,-200,-400,100],
    "y" : [0,0,-100,-100,-200],
    "settings" : [],
    "links" : [[0,1,0,2],[2,0,0,3],[3,2,0,0],[4,1,0,3]] # [node of output, node of input, output index, input index]
}

gear = {
    "tag" : 'GEAR',
    "name" : "Character gear",
    "desc" : "OFP2_ManSkeleton, ArmaMan, extra sections, copy model",
    "nodes" : ["MCFG_N_SkeletonPresetArmaman","MCFG_N_ModelPresetArmaman","MCFG_N_SectionList","MCFG_N_ModelPresetCopy"],
    "x" : [0,200,0,400],
    "y" : [0,0,-100,0],
    "settings" : [],
    "links" : [[0,1,0,0],[2,1,0,1],[1,3,0,0]]
}

weapon = {
    "tag" : 'WEAPON',
    "name" : "Weapon",
    "desc" : "Skeleton, common weapon bones, model, common weapon animations",
    "nodes" : [
        "MCFG_N_Skeleton",
        "MCFG_N_JoinList",
        "MCFG_N_BoneList",
        "MCFG_N_Bone",
        "MCFG_N_BoneListPresetStandardWeapon",
        "MCFG_N_Model",
        "MCFG_N_SectionList",
        "MCFG_N_AnimationList",
        "MCFG_N_AnimationPresetMuzzleflashRot",
        "MCFG_N_AnimationPresetSelectorRot",
        "MCFG_N_AnimationPresetTriggerRot",
        "MCFG_N_AnimationPresetMagazineHide"
    ],
    "x" : [0,-200,-400,-600,-400,300,0,0,-400,-400,-200,-200],
    "y" : [0,-100,0,0,-200,-100,-200,-400,-400,-600,-500,-700],
    "settings" : [
        [1,"listCount",2],
        [7,"animCount",4]
    ],
    "links" : [
        [0,5,0,2],
        [1,0,0,3],
        [2,1,0,0],
        [3,2,0,0],
        [4,1,0,1],
        [6,5,0,3],
        [7,5,0,4],
        [8,7,0,0],
        [9,7,0,1],
        [10,7,0,2],
        [11,7,0,3]
    ]
}

house = {
    "tag" : 'HOUSE',
    "name" : "House",
    "desc" : "Skeleton, preset bones list, model, sections list, preset animations",
    "nodes" : [
        "MCFG_N_Skeleton",
        "MCFG_N_Model",
        "MCFG_N_BoneListPresetHouse",
        "MCFG_N_JoinList",
        "MCFG_N_AnimationListPresetDoorsRot",
        "MCFG_N_AnimationListPresetGlasses",
        "MCFG_N_SectionList"
    ],
    "x" : [0,300,-200,100,-300,-100,-500],
    "y" : [0,-100,0,-300,-300,-400,-200],
    "settings" : [
        [3,"listCount",2]
    ],
    "links" : [
        [0,1,0,2],
        [2,0,0,3],
        [3,1,0,4],
        [4,3,0,0],
        [5,3,0,1],
        [6,1,0,3]
    ]
}

presets = [generic,gear,weapon,house]