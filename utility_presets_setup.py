import os
import sys
import bpy
import statistics
import json
from . import utility

###############################
####PRESET SETUP GENERATORS####
###############################

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
    
    bpy.context.scene.NodeSetupPresetList.clear()
    
    for setup in RawSetups:
        newItem = bpy.context.scene.NodeSetupPresetList.add()
        newItem.name = setup.get("name")
        newItem.desc = setup.get("desc")
        newItem.custom = setup.get("custom")
        newItem.path = setup.get("path")
    
    return

# Create custom preset file from current setup
def PresetTag(string):
    tag = string.strip()
    
    tag = "".join(filter(str.isalnum, tag))
    
    return tag

# Generate preset in dictionary format
def FormatPreset(context):
    
    nodeTree = context.space_data.node_tree
    
    # starting values
    tag = PresetTag(context.scene.modelCfgEditorPresetTag)
    name = context.scene.modelCfgEditorPresetName
    desc = context.scene.modelCfgEditorPresetDesc
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
    preset["tag"] = tag.upper()
    preset["name"] = name
    preset["desc"] = desc
    preset["nodes"] = nodes
    preset["x"] = x
    preset["y"] = y
    preset["settings"] = settings
    preset["links"] = links
    preset["postsettings"] = postsettings
    
    return preset

# Create setup preset from node tree
def CreatePreset(self,context):
    filepath = bpy.context.preferences.addons[__package__].preferences.customSetupPresets
    identifier = PresetTag(context.scene.modelCfgEditorPresetTag)
    
    # safety checks
    if identifier == "":
        utility.ShowInfoBox("Cannot create preset without identifier","Error",'ERROR')
        return
    
    existingSetups = PresetDefinitions()
    usedtags = []
    for setup in existingSetups:
        usedtags.append(setup.get("tag"))
    
    if identifier.upper() in usedtags:
        print("Used identifiers: " + ",".join(usedtags))
        reportFinal = "Check systemlog for used identifiers,"
        reportFinal += "|" + "conflicting identifier".upper()
        bpy.ops.mcfg.reportbox('INVOKE_DEFAULT',report=reportFinal)
        return
    
    # creating preset dictionary
    newSetup = FormatPreset(context)
    if newSetup == "":
        return
        
    # dumping to JSON
    outputfile = open(os.path.join(filepath,identifier.lower() + ".json"),"w")
    outputfile.write(json.dumps(newSetup,indent = 4))
    outputfile.close()

# Delete preset file
def DeletePreset(path):
    os.remove(path)
    ReloadPresets()