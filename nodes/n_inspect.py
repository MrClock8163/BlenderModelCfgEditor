import bpy
from bpy.types import Node
from .. import n_tree
from .. import utility_data as Data

class MCFG_N_Inspect(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Data inspector node'''
    
    # Mandatory variables
    bl_label = "Data inspector"
    bl_icon = 'VIEWZOOM'
    
    # Custom variables
    node_group = "operator"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Data-inspector"
    
    # Node properties
    active: bpy.props.BoolProperty(
        name = "Active",
        default = True
    )
    name: bpy.props.StringProperty(
        name = "Name",
        description = "Custom identifier name of inspector node",
        default = ""
    )
    inspect_id: bpy.props.IntProperty(
        name = "Inspector ID",
        description = "",
        default = 0,
        min = 0,
        max = 1000
    )
    
    # Custom function
    def GenerateInspectID(self,context):
        inspect_id_max = self.inspect_id
        for node in context.space_data.node_tree.nodes:
            if node.bl_idname == "MCFG_N_Inspect":
                inspect_id_max = max(node.inspect_id,inspect_id_max)
        
        return (inspect_id_max + 1)
        
    # Standard functions
    def draw_label(self):
        return "Inspector"
        
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_Universal', "Value")
        
        self.inspect_id = self.GenerateInspectID(bpy.context)

    def draw_buttons(self, context, layout):
        box = layout.box()
        box.label(text=("ID: " + str(self.inspect_id)))
        layout.prop(self,"name")
        layout.prop(self,"active")

    def copy(self, node):
        print("Copying from node ", node)
        self.inspect_id = self.GenerateInspectID(bpy.context)
        
    # Custom functions
    def GetInspectID(self):
        name = str(self.inspect_id)
        
        if self.name.strip() != "":
            name = self.name.strip()
            
        return name
    
    def inspect(self):
        if len(self.inputs[0].links) != 1 or not self.active:
            return
            
        print("==== Inspector output (ID: " + self.GetInspectID() + ") ====")
        self.inputs[0].links[0].from_node.inspect()