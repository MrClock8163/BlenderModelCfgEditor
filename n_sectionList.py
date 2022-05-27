import bpy
from bpy.types import Node
from . import n_tree
from . import utility
from .utility import NodeInfo, InfoItem, InfoTypes
# from . import utility_data as Data

class MCFG_N_SectionList(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Section list node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Section list"
    # Icon identifier
    bl_icon = 'NONE'
    
    node_group = "model"
    

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    
    def updateSectionCount(self,context):
        # print("List size changed")
        numberOfInputs = len(self.inputs)
        countDifference = self.sectionCount - numberOfInputs
        # print(countDifference)
        if countDifference < 0:
            for i in range(numberOfInputs-1,numberOfInputs-1 - abs(countDifference),-1):
                self.inputs.remove(self.inputs[i])
                # print("Remove input")
        else:
            for i in range(0,countDifference):
                # print("Add input")
                self.inputs.new('MCFG_S_ModelSection',"Section")
    
    sectionCount: bpy.props.IntProperty(
        name = "Section count",
        min = 1,
        max = 50,
        default = 1,
        update = updateSectionCount
    )
    
    
    #my_float_prop: bpy.props.FloatProperty(default=3.1415926)

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        self.customColor()
        
        self.inputs.new('MCFG_S_ModelSection', "Section")
        self.outputs.new('MCFG_S_ModelSectionList', "Section list")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        # layout.label(text="Node settings")
        layout.prop(self, "sectionCount")
        
    
    def process(self):
        sectionList = []
        
        for socket in self.inputs:
            newSection = ""
            if len(socket.links) != 0:
                newSection = socket.links[0].from_node.process()
            else:
                newSection = socket.stringValue.strip()
                
                
            if newSection != "":
                sectionList.append(newSection)
        
        return sectionList

    

    def draw_label(self):
        return "Section list"