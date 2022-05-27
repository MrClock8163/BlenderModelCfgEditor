from utility_data import Skeleton, Model, Bone, Animation, CfgSkeletons, CfgModels
# from utility_print import FilePrinter, ClassPrinter
from utility_print import ConfigFormatter, ConfigWriter
# from utility import ValidName, NodeErrorTypes
import os

newSkeleton = Skeleton("MRC_weapons_DC15S_skeleton","Default")
newModel = Model("DC15S")
newAnimation = Animation("magazine_hide")

newSkeleton.Set("skeletonInherit","asd")
newSkeleton.Set("isDiscrete",0)
# newSkeleton.Set("name","TestSkeleton")
# newSkeleton.Set("parent","none")


newSkeleton.AddBone(Bone("bone1",""))
newSkeleton.AddBone(Bone("bone2","bone1"))
# newSkeleton.Set("skeletonBones",-1)

print(newSkeleton.Get("skeletonBones"))
print(newSkeleton)
print(newModel)
print(newAnimation)

# print(FilePrinter.ClassOpen("MRC_base","Default"))

# print(float("hello"))
print(type(0) is str)

Printer = ConfigFormatter()

testVar = Printer.ParseStrTo("23,32,2,2675,-2",[0])

print(type(testVar))
print(testVar)

print("---------------------------------")


print(Printer.Property("testProp1",False,True,1))
# print(Printer.Property("testProp2",[0,2,3,1,2,421],[0],0,False,1))
print(Printer.Property("testProp2",["a","b",1,"d"],[""],0,False))

testVar2 = 0.1
print(type(testVar2)(2))

newSkeleton2 = Skeleton("TestSkelly","MRC_weapons_DC15S_skeleton")
newSkeleton2.Set("isDiscrete",-1)
newSkeleton2.Set("skeletonInherit",-1)
newSkeleton2.Set("skeletonBones",-1)

print(newSkeleton.Print())

print("---------------------------------")
print()


newModel = Model("DC15S","Default")
print(newModel.Print())

print("---------------------------------")
print()

newAnim = Animation("testAnim","")
newAnim.Set("animType","rotationX")
print(newAnim.Print(1))

print("---------------------------------")
print()

skeletonClass = Skeleton("Skeleton","")

# print(skeletonClass.Get("skeletonBones"))
skeletonClass.Set("isDiscrete",1)
skeletonClass.Set("skeletonInherit","")
skeletonClass.AddBone(Bone("bone1",""))
skeletonClass.AddBone(Bone("bone2",""))
skeletonClass.AddBone(Bone("bone3","bone2"))
skeletonClass.AddBone(Bone("bone4","bone2"))

modelClass = Model("Model","")
modelClass.Set("skeletonName","Skeleton")
modelClass.Set("sectionsInherit","")
# modelClass.Set("sections",[])
modelClass.AddSection("camo1")
modelClass.AddSection("camo2")
modelClass.AddSection("insignia")
animClass1 = Animation("anim1","")
modelClass.AddAnim(animClass1)
animClass2 = Animation("anim2","")
animClass2.Set("animType","hide")
modelClass.AddAnim(animClass2)

skeletonClasses = CfgSkeletons()
modelClasses = CfgModels()
skeletonClasses.AddSkeleton(skeletonClass)
skeletonClasses.AddSkeleton(newSkeleton)
modelClasses.AddModel(modelClass)
# print(skeletonClasses.Print())
# print(modelClasses.Print())

fileWriter = ConfigWriter("D:",[skeletonClasses,modelClasses])
fileWriter.WriteFile()

# print(skeletonClass.Get("skeletonBones"))

# print(skeletonClass.Print())
# print(modelClass.Print())
print("---------------------------------")
print()


print(os.path.exists("D:\BlenderModelCfgEditor"))

print("---------------------------------")
print()

# name = "MRC_weapons"

# if ValidName(name):
    # print("Correct name")
# else:
    # print(NodeErrorTypes.ClassName("node class"))

print("---------------------------------")
print()


skeletons = CfgSkeletons()
newSkeleton1 = Skeleton("Skeleton1","")
newSkeleton2 = Skeleton("Skeleton2","Skeleton4")
newSkeleton3 = Skeleton("Skeleton3","Skeleton2")
newSkeleton4 = Skeleton("Skeleton2","Skeleton2")

skeletons.AddSkeleton(newSkeleton3)
skeletons.AddSkeleton(newSkeleton2)
skeletons.AddSkeleton(newSkeleton1)
skeletons.AddSkeleton(newSkeleton4)

sortSuccess = skeletons.SortParenting()
print(sortSuccess)
print("All items are unique")
print(skeletons.Unique())
print(skeletons.Print())


print("---------------------------------")
print()

newBone = Bone("bone1","bone0")
newBone.Valid()