import os
import bpy
import statistics
from datetime import datetime
import json
from . import utility

#########################
#### LOAD AND INSERT ####
#########################

# Read and desirialize JSON file
def ReadPresetFile(path):

    jsonfile = open(path)
    preset = json.load(jsonfile)
    preset["path"] = path
    jsonfile.close()
    
    return preset

# Insert preset from given file
def InsertPreset(self,context,path):
    
    node_tree = context.space_data.node_tree
    preset = ReadPresetFile(path)
    
    # create nodes and set locations
    newNodeList = []
    for i in range(len(preset.get("nodes"))):
        newNode = node_tree.nodes.new(preset.get("nodes")[i])
        newNode.location = [preset.get("x")[i],preset.get("y")[i]]
        newNodeList.append(newNode)
    
    if len(newNodeList) == 0:
        return
    
    # process settings before trying to create links (important for list type nodes)
    for setting in preset.get("settings"):
        setattr(newNodeList[setting[0]],setting[1],setting[2])
    
    # create links
    for link in preset.get("links"):
        node_tree.links.new(newNodeList[link[0]].outputs[link[2]],newNodeList[link[1]].inputs[link[3]])
    
    # post settings after link creation (like inheritance properties)
    for setting in preset.get("postsettings"):
        setattr(newNodeList[setting[0]],setting[1],setting[2])
        
    return

# Get setup presets both built-in and custom
def PresetDefinitions():
    
    addonPrefs = bpy.context.preferences.addons[__package__].preferences
    dir_custom = addonPrefs.customSetupPresets
    dir_addon = os.path.join(os.path.dirname(os.path.realpath(__file__)),"setuppresets")
    
    # gather built-in files
    files = []
    
    for item in os.listdir(dir_addon):
        path = os.path.join(dir_addon,item)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == ".json":
                files.append(path)
    
    # gather external files
    if os.path.isdir(dir_custom):
        for item in os.listdir(dir_custom):
            path = os.path.join(dir_custom,item)
            if os.path.isfile(path):
                if os.path.splitext(path)[1] == ".json":
                    files.append(path)
    
    # read files
    returnpresets = []
    for file in files:
        returnpresets.append(ReadPresetFile(file))
    
    return returnpresets

# Load presets into UI list data
def ReloadPresets():
    RawSetups = PresetDefinitions()
    
    bpy.context.scene.MCFG_SP_PresetList.clear()
    
    for setup in RawSetups:
        newItem = bpy.context.scene.MCFG_SP_PresetList.add()
        newItem.name = setup.get("name")
        newItem.desc = setup.get("desc")
        newItem.custom = setup.get("custom")
        newItem.path = setup.get("path")
    
    return

# Delete preset file
def DeletePreset(path):
    os.remove(path)
    ReloadPresets()

##################
#### Generate ####
##################

# Generate preset in dictionary format
def FormatPreset(context):
    nodeTree = context.space_data.node_tree
    
    # starting values
    name = context.scene.MCFG_SP_PresetName
    desc = context.scene.MCFG_SP_PresetDesc
    nodes = []
    x = []
    y = []
    settings = []
    links = []
    postsettings = []
    
    if name == "":
        utility.ShowInfoBox("Cannot create preset without name","Error",'ERROR')
        return ""
    
    # populate nodes, x, y and settings
    for node in nodeTree.nodes:
        nodes.append(node.bl_idname)
        x.append(node.location[0])
        y.append(node.location[1])
        
        nodesettings = node.presetsettings()
        if len(nodesettings) != 0:
            for setting in nodesettings:
                settings.append([len(nodes) -1] + setting)
                
        nodesettingspost = node.presetpostsettings()
        if len(nodesettingspost) != 0:
            for setting in nodesettingspost:
                postsettings.append([len(nodes) -1] + setting)
    
    # populate links
    for link in nodeTree.links:
        nodeout = nodeTree.nodes.values().index(link.from_node)
        nodein = nodeTree.nodes.values().index(link.to_node)
        socketout = link.from_node.outputs.values().index(link.from_socket)
        socketin = link.to_node.inputs.values().index(link.to_socket)
        
        links.append([nodeout,nodein,socketout,socketin])
    
    # make the average location 0,0
    meanX = statistics.mean(x)
    meanY = statistics.mean(y)
    for i in range(len(nodes)):
        x[i] = int(round(x[i] - meanX,-1))
        y[i] = int(round(y[i] - meanY,-1))
    
    # creating dictionary
    preset = dict()
    preset["custom"] = True
    preset["name"] = name
    preset["desc"] = desc
    preset["nodes"] = nodes
    preset["x"] = x
    preset["y"] = y
    preset["settings"] = settings
    preset["links"] = links
    preset["postsettings"] = postsettings
    
    return preset

# Generate preset file name
def FormatPresetFileName():
    name = "setuppreset"
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    return (name + "_" + stamp)

# Create setup preset from node tree
def CreatePreset(self,context):
    addonPrefs = bpy.context.preferences.addons[__package__].preferences
    folderpath = addonPrefs.customSetupPresets
    filepath = os.path.join(folderpath,FormatPresetFileName() + ".json")
    
    # file name conflict handling
    if os.path.isfile(filepath) and not addonPrefs.customSetupPresetsReplace:
        utility.ShowInfoBox("File name conflict occured","Error",'ERROR')
        return
    
    # creating preset dictionary
    newSetup = FormatPreset(context)
    if newSetup == "":
        return
        
    outputfile = open(filepath,"w")
    outputfile.write(json.dumps(newSetup,indent = 4))
    outputfile.close()