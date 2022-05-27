from utility import NodeInfo, InfoItem, InfoTypes
from utility_data import Bone


infoclass = NodeInfo("Some random node")
infoclass.AddInfo(InfoItem(InfoTypes.ErrClassName("MRC_weapons_")))
infoclass.AddInfo(InfoItem("no further errors were found","i"))
infoclass.AddInfo(InfoItem("there are unconnected nodes in the tree","w"))

infoclass.Print(True)


print(Bone("bone1","bone0"))