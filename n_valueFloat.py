import bpy
from bpy.types import Node
from . import n_tree

class MCFG_N_ValueFloat(Node, n_tree.MCFG_N_Base):
    @classmethod
    def poll(cls,ntree):
        return ntree.bl_idname == 'MCFG_N_Tree'
    # === Basics ===
    # Description string
    '''Float input node'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    #bl_idname = 'CustomNodeType'
    # Label for nice name display
    bl_label = "Float input"
    # Icon identifier
    bl_icon = 'NONE'
    
    node_group = "value"


    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    
    
    floatProperty: bpy.props.FloatProperty(
        name = "Value",
        default = 0.0,
        min = -100,
        max = 100,
        soft_max = 50,
        soft_min = -50
    )

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        self.customColor()
        self.outputs.new('MCFG_S_ValueFloat', "Value")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        # layout.label(text="Node settings")
        layout.prop(self, "floatProperty")

    def process(self):
        return self.floatProperty

    # Detail buttons in the sidebar.
    # If this function is not defined, the draw_buttons function is used instead
    #def draw_buttons_ext(self, context, layout):
        #layout.prop(self, "my_float_prop")
        # my_string_prop button will only be visible in the sidebar

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Float"