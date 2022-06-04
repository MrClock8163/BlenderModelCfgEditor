preset = {
	"tag" : "EXAMPLE",                                  # unique identifier of the preset
	"name" : "Example preset",                          # visible name
	"desc" : "Example file for a custom preset",        # description of the preset
	"nodes" : [                                         # list of nodes in the preset indentified by their python class names
		"MCFG_N_Skeleton",
		"MCFG_N_Model",
		"MCFG_N_BoneList",
		"MCFG_N_Bone",
		"MCFG_N_Bone",
		"MCFG_N_SectionList",
		"MCFG_N_AnimationList",
		"MCFG_N_AnimationTranslation"
	],
	"x" : [110,410,-90,-290,-290,110,110,-90],          # node editor space X coordinates of nodes
	"y" : [180,180,80,80,-60,-20,-200,-220],            # node editor space Y coordinates of nodes
	"settings" : [                                      # settings to apply to nodes before links are created (especially important for list type nodes)
		[2,"boneCount",2],                              # [index of node in nodes list,"property name",property value]
		[5,"sectionCount",3],
		[7,"axisType","POINTS"]
	],
	"links" : [                                         # links to create between the nodes of the preset
		[0,1,0,2],                                      # [index of node of output,index of node of input,index of output socket,index of input socket]
		[2,0,0,3],
		[3,2,0,0],
		[5,1,0,3],
		[4,2,0,1],
		[3,4,0,0],
		[6,1,0,4],
		[7,6,0,0]
	]
}
