# Example custom node script for the Arma 3 model config editor addon.
# The following code is to demostrate how the Custom script node can be used.
#
# The code expects the following node settings and inputs:
#       - Inputs: 2
#       - Input[0]: Bone item node providing a bone parent
#       - Input[1]: String input node providing a bone name base ("%" character indicating where the generated index should be inserted
#       - Input[2]: number of bones to generate
# 
# Result:
# The script generates 10 bones, similar to how the Bone list - generator node functions. The bones will be generated witht the given base name,
# and parented to the given bone

import BlenderModelCfgEditor.utility_data as Data # module that defines the Bone class the addon uses for data conversion

baseBone = input_0
if input_0 != "":
    baseBone = input_0.name.strip() # the inputs of the node are accessable through the input_## variables

baseName = input_1.strip()

if baseName == "":
    exit()

boneCount = input_2
if input_2 == "":
    boneCount = 10

newBones = []

for i in range(int(round(boneCount,0))):
    index = str(i + 1)
    newBones.append(Data.Bone(baseName.replace("%",index),baseBone))

result = newBones # the returned value must be assigned to a variable called 'result'