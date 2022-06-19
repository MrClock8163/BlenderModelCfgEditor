#    ----------------------------------------------------------------------------------------
#    
#    This is a sample script to demostrate the use of the Custom script node.
#    The code shows the use of inputs, outputs and custom data operations.
#    The result is similar to that of the Bone list - generator node. The script generates a list of bone items with the given parent and base name.
#    For more information on the topic, visit the addon wiki site https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Custom-script.
#    
#    ---------------------------------------- HEADER ----------------------------------------
#    
#    Author: MrClock
#    Addon: Arma 3 model config editor
#    Name: Example custom node script
#    
#    Description:
#        Generates a list of bones with increasing indices.
#    
#    Node inputs:
#        - 0: Bone item or String input node providing a bone parent name (can be empty, but the socket must be present)
#        - 1: String input node providing a bone name base ("%" character indicating where the generated index should be inserted)
#        - 2: Float input node providing the number of bones to generate (defaults to 10 if left without input)
#    
#    Return value:
#        - list of bones
#    
#    ----------------------------------------------------------------------------------------

import BlenderModelCfgEditor.utility_data as Data # module that defines the classes the addon uses for translating the node setup into the desired format

baseBone = input_0 # the inputs of the node are accessable through the input_#INDEX# variables
if type(input_0) is not str:
    baseBone = input_0.name.strip()

baseName = input_1.strip()

if baseName != "":
    boneCount = input_2
    if input_2 == "":
        boneCount = 10

    newBones = []

    for i in range(int(round(boneCount,0))):
        index = str(i + 1)
        newBones.append(Data.Bone(baseName.replace("%",index),baseBone))

    result = newBones # the returned value must be assigned to a variable called 'result'