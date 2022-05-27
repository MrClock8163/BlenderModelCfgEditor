import bpy
from bpy.types import Node
from . import n_tree
from . import utility
from .utility import NodeInfo, InfoItem, InfoTypes

class MCFG_N_Section(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Section item node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Section item"
    # Icon identifier
    bl_icon = 'MESH_DATA'
    
    node_group = "model"


    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    
    sectionName: bpy.props.StringProperty(
        default="Section",
        name="Name",
        description = "Name of the section\nNaming rules:\n-must be unique\n-must start with letter\n-no speical characters"
    )
    
    def getSectionName(self):
        return self.sectionName.strip()
    
    #my_float_prop: bpy.props.FloatProperty(default=3.1415926)

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        self.customColor()
 
        self.outputs.new('MCFG_S_ModelSection', "Section")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        # layout.label(text="Node settings")
        layout.prop(self, "sectionName")

    def process(self):
        return self.getSectionName()
        
    def draw_label(self):
        return "Section"