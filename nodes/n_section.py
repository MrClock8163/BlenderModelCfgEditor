import bpy
from bpy.types import Node
from .. import n_tree

class MCFG_N_Section(Node, n_tree.MCFG_N_Base):
    # Description string
    '''Section item node'''
    
    # Mandatory variables
    bl_label = "Section item"
    bl_icon = 'MESH_DATA'
    
    # Custom variables
    node_group = "section"
    doc_url = "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki/Node:-Section-item"
    
    # Node properties
    def updateSectionName(self,context):
        self.name = "Section: {}".format(self.sectionName)
    
    sectionName: bpy.props.StringProperty(
        default="Section",
        name="Name",
        description = "Name of the section",
        update = updateSectionName
    )
    
    # Standard functions
    def draw_label(self):
        return "Section"
        
    def init(self, context):
        self.customColor()
 
        self.outputs.new('MCFG_S_ModelSection', "Section")

    def draw_buttons(self, context, layout):
        layout.prop(self, "sectionName")
        
    # Custom functions
    def getSectionName(self):
        return self.sectionName.strip()

    def process(self):
        return self.getSectionName()
        
    def inspect(self):
        print(self.process())