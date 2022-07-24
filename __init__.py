bl_info = {
    "name": "Arma 3 model.cfg node editor",
    "author": "MrClock",
    "version": (0, 0, 1),
    "blender": (2, 83, 0),
    "location": "Model config editor",
    "description": "Node tree based tool for creating model configuration files",
    "warning": "Not a release (work in progress)",
    # "tracker_url": "",
    # "support": "TESTING",
    "doc_url": "https://github.com/MrClock8163/BlenderModelCfgEditor/wiki",
    "category": "Node"
}

if "bpy" in locals():
    import importlib
    
    # Nodes
    importlib.reload(nodes.n_animation)
    importlib.reload(nodes.n_animationList)
    importlib.reload(nodes.n_bone)
    importlib.reload(nodes.n_boneList)
    importlib.reload(nodes.n_compareFloat)
    importlib.reload(nodes.n_demostrative)
    importlib.reload(nodes.n_inspect)
    importlib.reload(nodes.n_joinList)
    importlib.reload(nodes.n_logicBasic)
    importlib.reload(nodes.n_mathBasic)
    importlib.reload(nodes.n_mathExpression)
    importlib.reload(nodes.n_model)
    importlib.reload(nodes.n_scripted)
    importlib.reload(nodes.n_section)
    importlib.reload(nodes.n_sectionList)
    importlib.reload(nodes.n_parent)
    importlib.reload(nodes.n_skeleton)
    importlib.reload(nodes.n_valueFloat)
    importlib.reload(nodes.n_valueString)
    
    # Node presets
    importlib.reload(nodepresets.n_animationListPresetBullets)
    importlib.reload(nodepresets.n_animationListPresetCar)
    importlib.reload(nodepresets.n_animationListPresetDoors)
    importlib.reload(nodepresets.n_animationListPresetGlasses)
    importlib.reload(nodepresets.n_animationListPresetTank)
    importlib.reload(nodepresets.n_animationListPresetTurret)
    importlib.reload(nodepresets.n_animationPresetMagazine)
    importlib.reload(nodepresets.n_animationPresetMuzzleflash)
    importlib.reload(nodepresets.n_animationPresetSelector)
    importlib.reload(nodepresets.n_animationPresetSight)
    importlib.reload(nodepresets.n_animationPresetTrigger)
    importlib.reload(nodepresets.n_boneListPresetCar)
    importlib.reload(nodepresets.n_boneListPresetGenerate)
    importlib.reload(nodepresets.n_boneListPresetHouse)
    importlib.reload(nodepresets.n_boneListPresetReplace)
    importlib.reload(nodepresets.n_boneListPresetStandards)
    importlib.reload(nodepresets.n_boneListPresetSymmetrize)
    importlib.reload(nodepresets.n_boneListPresetTank)
    importlib.reload(nodepresets.n_boneListPresetTurret)
    importlib.reload(nodepresets.n_modelPresetArmaman)
    importlib.reload(nodepresets.n_modelPresetCopy)
    importlib.reload(nodepresets.n_modelPresetDefault)
    importlib.reload(nodepresets.n_skeletonPresetArmaman)
    importlib.reload(nodepresets.n_skeletonPresetDefault)
    
    # Sockets
    importlib.reload(sockets.s_list)
    importlib.reload(sockets.s_modelAnimation)
    importlib.reload(sockets.s_modelAnimationList)
    importlib.reload(sockets.s_modelParent)
    importlib.reload(sockets.s_modelSection)
    importlib.reload(sockets.s_modelSectionList)
    importlib.reload(sockets.s_modelSourceAddress)
    importlib.reload(sockets.s_skeletonBone)
    importlib.reload(sockets.s_skeletonBoneList)
    importlib.reload(sockets.s_skeletonParent)
    importlib.reload(sockets.s_universal)
    importlib.reload(sockets.s_valueBool)
    importlib.reload(sockets.s_valueFloat)
    importlib.reload(sockets.s_valueString)
    
    # Misc
    importlib.reload(n_tree)
    importlib.reload(ui)
    importlib.reload(utility)
    importlib.reload(utility_data)
    importlib.reload(utility_presets)
    importlib.reload(utility_presets_setup)
    importlib.reload(utility_import)
    importlib.reload(utility_import_xml)

else:
    # Nodes
    from . nodes import n_animation
    from . nodes import n_animationList
    from . nodes import n_bone
    from . nodes import n_boneList
    from . nodes import n_compareFloat
    from . nodes import n_demostrative
    from . nodes import n_inspect
    from . nodes import n_joinList
    from . nodes import n_logicBasic
    from . nodes import n_mathBasic
    from . nodes import n_mathExpression
    from . nodes import n_model
    from . nodes import n_scripted
    from . nodes import n_section
    from . nodes import n_sectionList
    from . nodes import n_parent
    from . nodes import n_skeleton
    from . nodes import n_valueFloat
    from . nodes import n_valueString
    
    # Node presets
    from . nodepresets import n_animationListPresetBullets
    from . nodepresets import n_animationListPresetCar
    from . nodepresets import n_animationListPresetDoors
    from . nodepresets import n_animationListPresetGlasses
    from . nodepresets import n_animationListPresetTank
    from . nodepresets import n_animationListPresetTurret
    from . nodepresets import n_animationPresetMagazine
    from . nodepresets import n_animationPresetMuzzleflash
    from . nodepresets import n_animationPresetSelector
    from . nodepresets import n_animationPresetSight
    from . nodepresets import n_animationPresetTrigger
    from . nodepresets import n_boneListPresetCar
    from . nodepresets import n_boneListPresetGenerate
    from . nodepresets import n_boneListPresetHouse
    from . nodepresets import n_boneListPresetReplace
    from . nodepresets import n_boneListPresetStandards
    from . nodepresets import n_boneListPresetSymmetrize
    from . nodepresets import n_boneListPresetTank
    from . nodepresets import n_boneListPresetTurret
    from . nodepresets import n_modelPresetArmaman
    from . nodepresets import n_modelPresetCopy
    from . nodepresets import n_modelPresetDefault
    from . nodepresets import n_skeletonPresetArmaman
    from . nodepresets import n_skeletonPresetDefault
    
    # Sockets
    from . sockets import s_list
    from . sockets import s_modelAnimation
    from . sockets import s_modelAnimationList
    from . sockets import s_modelParent
    from . sockets import s_modelSection
    from . sockets import s_modelSectionList
    from . sockets import s_modelSourceAddress
    from . sockets import s_skeletonBone
    from . sockets import s_skeletonBoneList
    from . sockets import s_skeletonParent
    from . sockets import s_universal
    from . sockets import s_valueBool
    from . sockets import s_valueFloat
    from . sockets import s_valueString
    
    # Misc
    from . import n_tree
    from . import ui
    from . import utility
    from . import utility_data
    from . import utility_presets
    from . import utility_presets_setup
    from . import utility_import
    from . import utility_import_xml

import bpy
import os

# Addon preferences update handlers
def updateCustomSetupPresets(self,context):
    utility_presets_setup.ReloadPresets()

# Addon preferences
class MCFG_AT_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    
    # Tab selection
    tabs: bpy.props.EnumProperty(
        name = "Tabs",
        description = "",
        default = 'GENERAL',
        items = (
            ('GENERAL',"General","General and misc settings",'PREFERENCES',0),
            ('COLOR',"Colors","Color settings",'COLOR',1),
            ('VALIDATION',"Validation","Validation settings",'CHECKMARK',2),
            ('PRESETS',"Presets","Setup preset settings",'PRESET',3)
        )
    )
    
    # Arma 3 Tools settings
    armaToolsFolder: bpy.props.StringProperty(
        description = "Install directory of the official Arma 3 Tools",
        name = "Path",
        default = "",
        subtype = 'DIR_PATH'
    )
    
    # Color settings
    useCustomColors: bpy.props.BoolProperty(
        description = "Display nodes belonging to the distinct categories with unique background colors.",
        name = "Node background colors",
        default = True
    )
    customColorSkeleton: bpy.props.FloatVectorProperty(
        name = "Skeleton",
        description = "Color used for skeleton related nodes",
        subtype = 'COLOR',
        default = (0.792, 0.322, 0.067),
        min = 0.0,
        max = 1.0
    )
    customColorBones: bpy.props.FloatVectorProperty(
        name = "Bone",
        description = "Color used for bone related nodes",
        subtype = 'COLOR',
        default = (0.902, 0.271,0.333),
        min = 0.0,
        max = 1.0
    )
    customColorModel: bpy.props.FloatVectorProperty(
        name = "Model",
        description = "Color used for model related nodes",
        subtype = 'COLOR',
        default = (0.0, 0.7, 1.0),
        min = 0.0,
        max = 1.0
    )
    customColorSection: bpy.props.FloatVectorProperty(
        name = "Section",
        description = "Color used for section related nodes",
        subtype = 'COLOR',
        default = (0.0, 0.7, 0),
        min = 0.0,
        max = 1.0
    )
    customColorAnimations: bpy.props.FloatVectorProperty(
        name = "Animation",
        description = "Color used for animation related nodes",
        subtype = 'COLOR',
        default = (0, 0.4,1.0),
        min = 0.0,
        max = 1.0
    )
    customColorOperator: bpy.props.FloatVectorProperty(
        name = "Operator and misc",
        description = "Color used for operation related nodes",
        subtype = 'COLOR',
        default = (0.4, 0.4,0.4),
        min = 0.0,
        max = 1.0
    )
    
    # Validation settings
    validationOutput: bpy.props.EnumProperty(
        name = "Log",
        description = "Where the validation log should be written in case the validation fails.",
        items = (
            ('CONSOLE',"System console","Output the log to Blender's system console",'CONSOLE',0),
            ('FILE',"Log file","Output the log to a .log text file in the export directory",'TEXT',1)
        ),
        default = 'CONSOLE'
    )
    warnsAreErr: bpy.props.BoolProperty(
        name = "Warnings are errors",
        description = "Treat warnings as errors when evaluting the validation results.",
        default = True
    )
    
    # Preset settings
    customSetupPresets: bpy.props.StringProperty(
        name="Custom setup presets", 
        description="Folder that contains the .json files describing custom setup presets", 
        subtype='DIR_PATH',
        default="",
        update=updateCustomSetupPresets
    )
    customSetupPresetsReplace: bpy.props.BoolProperty(
        name="Replace old",
        description="Replace the old preset file with the new one if name conflict occurs during generation (the probability is practically zero, but the possibility cannot be ruled out)",
        default=True
    )
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row(align=True)
        row.prop(self,"tabs",expand=True)
        
        box = layout.box()
        
        if self.tabs == 'GENERAL':
            grid = box.grid_flow(align=True,columns=2,row_major=True,even_columns=True,even_rows=True)
            grid.label(text="Arma 3 Tools")
            grid.prop(self,"armaToolsFolder",text="")
            
        if self.tabs == 'COLOR':
            box.prop(self,"useCustomColors",toggle=True)
            
            if self.useCustomColors:
                grid = box.grid_flow(align=True,columns=2,row_major=True,even_columns=True,even_rows=True)
                
                grid.label(text="Operator and misc")
                grid.prop(self,"customColorOperator",text="")
                
                grid.label(text="Skeleton")
                grid.prop(self,"customColorSkeleton",text="")
                
                grid.label(text="Bone")
                grid.prop(self,"customColorBones",text="")
                
                grid.label(text="Model")
                grid.prop(self,"customColorModel",text="")
                
                grid.label(text="Section")
                grid.prop(self,"customColorSection",text="")
                
                grid.label(text="Animation")
                grid.prop(self,"customColorAnimations",text="")
                
        if self.tabs == 'VALIDATION':
            grid = box.grid_flow(align=True,columns=2,row_major=True,even_columns=True,even_rows=True)
            grid.label(text="Warnings are errors")
            grid.prop(self,"warnsAreErr",text="")
            # row = box.row(align=True)
            grid.label(text="Output")
            row = grid.row(align=True)
            row.prop(self,"validationOutput",expand=True)
            
        if self.tabs == 'PRESETS':
            grid = box.grid_flow(align=True,columns=2,row_major=True,even_columns=True,even_rows=True)
            grid.label(text="Replace old")
            grid.prop(self,"customSetupPresetsReplace",text="")
            grid.label(text="Presets folder")
            grid.prop(self,"customSetupPresets",text="")
        
import nodeitems_utils
from nodeitems_utils import NodeItem

# node menu
node_categories = [
    n_tree.MCFG_N_Category('SKELETONNODES', "Skeleton", items=[
        NodeItem("MCFG_N_Skeleton")
    ]),
    n_tree.MCFG_N_Category('SKELETONPRESETNODES', "Skeleton preset", items=[
        NodeItem("MCFG_N_SkeletonPresetDefault"),
        NodeItem("MCFG_N_SkeletonPresetArmaman")
    ]),
    n_tree.MCFG_N_Category('MODELNODES', "Model", items=[
        NodeItem("MCFG_N_Model")
    ]),
    n_tree.MCFG_N_Category('MODELPRESETNODES', "Model preset", items=[
        NodeItem("MCFG_N_ModelPresetDefault"),
        NodeItem("MCFG_N_ModelPresetCopy"),
        NodeItem("MCFG_N_ModelPresetArmaman")
    ]),
    n_tree.MCFG_N_Category('BONENODES', "Bone", items=[
        NodeItem("MCFG_N_Bone"),
        NodeItem("MCFG_N_BoneList")
    ]),
    n_tree.MCFG_N_Category('BONEPRESETNODES', "Bone preset", items=[
        NodeItem("MCFG_N_BoneListPresetStandardWeapon"),
        NodeItem("MCFG_N_BoneListPresetHouse"),
        NodeItem("MCFG_N_BoneListPresetGenerate"),
        NodeItem("MCFG_N_BoneListPresetReplace"),
        NodeItem("MCFG_N_BoneListPresetSymmetrize"),
        NodeItem("MCFG_N_BoneListPresetTank"),
        NodeItem("MCFG_N_BoneListPresetCar"),
        NodeItem("MCFG_N_BoneListPresetTurret")
    ]),
    n_tree.MCFG_N_Category('SECTIONNODES', "Section", items=[
        NodeItem("MCFG_N_Section"),
        NodeItem("MCFG_N_SectionList")
    ]),
    n_tree.MCFG_N_Category('ANIMATIONNODES', "Animation", items=[
        NodeItem("MCFG_N_Animation", label = "Animation class - translation", settings = {"animType": repr("TRANSLATION")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - translation X", settings = {"animType": repr("TRANSLATIONX")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - translation Y", settings = {"animType": repr("TRANSLATIONY")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - translation Z", settings = {"animType": repr("TRANSLATIONZ")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - rotation", settings = {"animType": repr("ROTATION")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - rotation X", settings = {"animType": repr("ROTATIONX")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - rotation Y", settings = {"animType": repr("ROTATIONY")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - rotation Z", settings = {"animType": repr("ROTATIONZ")}),
        NodeItem("MCFG_N_Animation", label = "Animation class - hide", settings = {"animType": repr("HIDE")}),
        NodeItem("MCFG_N_AnimationList")
    ]),
    n_tree.MCFG_N_Category('ANIMATIONPRESETNODES', "Animation preset", items=[
        NodeItem("MCFG_N_AnimationPresetMuzzleflashRot"),
        NodeItem("MCFG_N_AnimationPresetTriggerRot"),
        NodeItem("MCFG_N_AnimationPresetTriggerMove"),
        NodeItem("MCFG_N_AnimationPresetSelectorRot"),
        NodeItem("MCFG_N_AnimationPresetSightHide"),
        NodeItem("MCFG_N_AnimationPresetMagazineHide"),
        NodeItem("MCFG_N_AnimationListPresetBulletsHide"),
        NodeItem("MCFG_N_AnimationListPresetDoorsRot"),
        NodeItem("MCFG_N_AnimationListPresetDoorsMove"),
        NodeItem("MCFG_N_AnimationListPresetGlasses"),
        NodeItem("MCFG_N_AnimationListPresetTank"),
        NodeItem("MCFG_N_AnimationListPresetCarWheels"),
        NodeItem("MCFG_N_AnimationListPresetCarWheelsSteer"),
        NodeItem("MCFG_N_AnimationListPresetTurret")
    ]),
    n_tree.MCFG_N_Category('OPERATORNODES', "Operator", items=[
        NodeItem("MCFG_N_JoinList"),
        NodeItem("MCFG_N_ValueFloat"),
        NodeItem("MCFG_N_CompareFloat"),
        NodeItem("MCFG_N_ValueString"),
        NodeItem("MCFG_N_MathBasic"),
        NodeItem("MCFG_N_LogicBasic")
    ]),
    n_tree.MCFG_N_Category('MISCNODES', "Miscellaneous", items=[
        NodeItem("MCFG_N_Inspect"),
        NodeItem("MCFG_N_Scripted"),
        NodeItem("MCFG_N_MathExpression"),
        NodeItem("MCFG_N_Parent"),
        NodeItem("MCFG_N_Demostrative")
    ]),
    n_tree.MCFG_N_Category('LAYOUTNODES', "Layout", items=[
        NodeItem("NodeFrame")
    ])
]

# Registration

# Nodes
classes_node = (
    nodes.n_animation.MCFG_N_Animation,
    nodes.n_animationList.MCFG_N_AnimationList,
    nodes.n_bone.MCFG_N_Bone,
    nodes.n_boneList.MCFG_N_BoneList,
    nodes.n_compareFloat.MCFG_N_CompareFloat,
    nodes.n_demostrative.MCFG_N_Demostrative,
    nodes.n_inspect.MCFG_N_Inspect,
    nodes.n_joinList.MCFG_N_JoinList,
    nodes.n_logicBasic.MCFG_N_LogicBasic,
    nodes.n_mathBasic.MCFG_N_MathBasic,
    nodes.n_mathExpression.MCFG_N_MathExpression,
    nodes.n_model.MCFG_N_Model,
    nodes.n_scripted.MCFG_N_Scripted,
    nodes.n_section.MCFG_N_Section,
    nodes.n_sectionList.MCFG_N_SectionList,
    nodes.n_parent.MCFG_N_Parent,
    nodes.n_skeleton.MCFG_N_Skeleton,
    nodes.n_valueFloat.MCFG_N_ValueFloat,
    nodes.n_valueString.MCFG_N_ValueString
)
# Node presets
classes_presetnode = (
    nodepresets.n_animationListPresetBullets.MCFG_N_AnimationListPresetBulletsHide,
    nodepresets.n_animationListPresetCar.MCFG_N_AnimationListPresetCarWheels,
    nodepresets.n_animationListPresetCar.MCFG_N_AnimationListPresetCarWheelsSteer,
    nodepresets.n_animationListPresetDoors.MCFG_N_AnimationListPresetDoorsRot,
    nodepresets.n_animationListPresetDoors.MCFG_N_AnimationListPresetDoorsMove,
    nodepresets.n_animationListPresetGlasses.MCFG_N_AnimationListPresetGlasses,
    nodepresets.n_animationListPresetTank.MCFG_N_AnimationListPresetTank,
    nodepresets.n_animationListPresetTurret.MCFG_N_AnimationListPresetTurret,
    nodepresets.n_animationPresetMagazine.MCFG_N_AnimationPresetMagazineHide,
    nodepresets.n_animationPresetMuzzleflash.MCFG_N_AnimationPresetMuzzleflashRot,
    nodepresets.n_animationPresetSelector.MCFG_N_AnimationPresetSelectorRot,
    nodepresets.n_animationPresetSight.MCFG_N_AnimationPresetSightHide,
    nodepresets.n_animationPresetTrigger.MCFG_N_AnimationPresetTriggerRot,
    nodepresets.n_animationPresetTrigger.MCFG_N_AnimationPresetTriggerMove,
    nodepresets.n_boneListPresetCar.MCFG_N_BoneListPresetCar,
    nodepresets.n_boneListPresetGenerate.MCFG_N_BoneListPresetGenerate,
    nodepresets.n_boneListPresetHouse.MCFG_N_BoneListPresetHouse,
    nodepresets.n_boneListPresetReplace.MCFG_N_BoneListPresetReplace,
    nodepresets.n_boneListPresetStandards.MCFG_N_BoneListPresetStandardWeapon,
    nodepresets.n_boneListPresetSymmetrize.MCFG_N_BoneListPresetSymmetrize,
    nodepresets.n_boneListPresetTank.MCFG_N_BoneListPresetTank,
    nodepresets.n_boneListPresetTurret.MCFG_N_BoneListPresetTurret,
    nodepresets.n_modelPresetArmaman.MCFG_N_ModelPresetArmaman,
    nodepresets.n_modelPresetCopy.MCFG_N_ModelPresetCopy,
    nodepresets.n_modelPresetDefault.MCFG_N_ModelPresetDefault,
    nodepresets.n_skeletonPresetArmaman.MCFG_N_SkeletonPresetArmaman,
    nodepresets.n_skeletonPresetDefault.MCFG_N_SkeletonPresetDefault
)
# Sockets
classes_socket = (
    sockets.s_list.MCFG_S_List,
    sockets.s_modelAnimation.MCFG_S_ModelAnimation,
    sockets.s_modelAnimationList.MCFG_S_ModelAnimationList,
    sockets.s_modelParent.MCFG_S_ModelParent,
    sockets.s_modelSection.MCFG_S_ModelSection,
    sockets.s_modelSectionList.MCFG_S_ModelSectionList,
    sockets.s_modelSourceAddress.MCFG_S_ModelSourceAddress,
    sockets.s_skeletonBone.MCFG_S_SkeletonBone,
    sockets.s_skeletonBoneList.MCFG_S_SkeletonBoneList,
    sockets.s_skeletonParent.MCFG_S_SkeletonParent,
    sockets.s_universal.MCFG_S_Universal,
    sockets.s_valueBool.MCFG_S_ValueBool,
    sockets.s_valueFloat.MCFG_S_ValueFloat,
    sockets.s_valueString.MCFG_S_ValueString
)
# Misc
classes_misc = (
    MCFG_AT_Preferences,
    n_tree.MCFG_N_Tree,
    ui.MCFG_MT_TemplatesNodeScript,
    ui.MCFG_MT_TemplatesSetupPresets,
    ui.MCFG_GT_ModelSelectionItem,
    ui.MCFG_GT_NodeSetupPresetItem,
    ui.MCFG_UL_ModelSelectionList,
    ui.MCFG_UL_NodeSetupPresetList,
    ui.MCFG_OT_BonesFromModel,
    ui.MCFG_OT_SectionsFromModel,
    ui.MCFG_OT_ReportBox,
    ui.MCFG_OT_Import,
    ui.MCFG_OT_Export,
    ui.MCFG_OT_Validate,
    ui.MCFG_OT_LoadPresets,
    ui.MCFG_OT_InsertPreset,
    ui.MCFG_OT_CreatePreset,
    ui.MCFG_OT_DeletePreset,
    ui.MCFG_OT_Inspect,
    ui.MCFG_PT_Tools,
    ui.MCFG_PT_Import,
    ui.MCFG_PT_Export,
    ui.MCFG_PT_Presets,
    ui.MCFG_PT_Docs
)

def register():
    from bpy.utils import register_class
    
    print("Registering Model Cfg editor ( '" + __name__ + "' )")

    for cls in classes_node:
        register_class(cls)
    print("\tnode\t\t" + str(len(classes_node)))

    for cls in classes_presetnode:
        register_class(cls)
    print("\tpreset node\t" + str(len(classes_presetnode)))

    for cls in classes_socket:
        register_class(cls)
    print("\tsocket\t\t" + str(len(classes_socket)))

    for cls in classes_misc:
        register_class(cls)
    print("\tmisc\t\t" + str(len(classes_misc)))

    nodeitems_utils.register_node_categories('MCFG_NODES', node_categories)
    
    print("\tproperties")
    
    # Panel settings
    bpy.types.Scene.MCFG_SP_ImportDepth = bpy.props.EnumProperty (
        name = "Import depth",
        description = "How deep the import should go",
        items = (
            ('SKELETONS',"Only skeletons","Import only the skeletons"),
            ('MODELS',"Skeletons and models","Import skeletons and models, omit animations"),
            ('ANIMS',"All","Import all data")
        ),
        default = 'ANIMS'
    )
    bpy.types.Scene.MCFG_SP_ImportLinkDepth = bpy.props.EnumProperty (
        name = "Links",
        description = "What level of node links should be created",
        items = (
            ('NONE',"None","Don't create any links between nodes"),
            ('ESSENTIAL',"Only essentials","Only create essential and unique connections (e.g.: parenting, unique data, but no links to list nodes"),
            ('ALL',"All","Create all links")
        ),
        default = 'ALL'
    )
    bpy.types.Scene.MCFG_SP_ImportExpressions = bpy.props.EnumProperty(
        name = "Expressions",
        description = "",
        items = (
            ('EVAL',"Evaluate","Evaluate all expressions"),
            ('PRESERVE',"Preserve","Preserve each floating point number value as simple expression"),
            ('AUTO',"Auto","Evaluate raw numbers, preserve actual expressions")
        ),
        default = 'EVAL'
    )
    bpy.types.Scene.MCFG_SP_ExportDir = bpy.props.StringProperty (
        name = "Directory",
        description = "Directory to save file to",
        default = "",
        subtype = 'DIR_PATH'
    )
    bpy.types.Scene.MCFG_SP_IgnoreErrors = bpy.props.BoolProperty (
        name = "Ignore errors",
        description = "(NOT RECOMMENDED, use only for debugging) Ignore the result of validation and export the config regardless",
        default = False
    )
    bpy.types.Scene.MCFG_SP_OpenFile = bpy.props.BoolProperty (
        name = "Open file",
        description = "Open config in the default program after export",
        default = False
    )
    bpy.types.Scene.MCFG_SP_PresetName = bpy.props.StringProperty (
        name = "Name",
        description = "Name of the preset to be created",
        default = "Untitled preset"
    )
    bpy.types.Scene.MCFG_SP_PresetDesc = bpy.props.StringProperty (
        name = "Description",
        description = "Description of the preset to be created",
        default = ""
    )
    
    # Container properties
    bpy.types.Scene.MCFG_SP_ModelSelectionList = bpy.props.CollectionProperty(type=ui.MCFG_GT_ModelSelectionItem)
    bpy.types.Scene.MCFG_SP_ModelSelectionListIndex = bpy.props.IntProperty(name = "Selection index",default = 0)
    bpy.types.Scene.MCFG_SP_ModelSelectionListListNode = bpy.props.BoolProperty(name = "Create list node",default = False)
    bpy.types.Scene.MCFG_SP_PresetList = bpy.props.CollectionProperty(type=ui.MCFG_GT_NodeSetupPresetItem)
    bpy.types.Scene.MCFG_SP_PresetListIndex = bpy.props.IntProperty(name = "Selection index",default = 0)
    
    # Node properties
    bpy.types.NodeFrame.process_type = ""
    bpy.types.NodeFrame.doc_url = ""
    
    print("\tmenus")
    
    # Menus
    bpy.types.NODE_MT_editor_menus.append(ui.draw_header)
    bpy.types.TEXT_MT_templates.append(ui.draw_menu)
    
    print("Register done")

def unregister():
    from bpy.utils import unregister_class
    
    print("Unregistering Model Cfg editor ( '" + __name__ + "' )")
    
    nodeitems_utils.unregister_node_categories('MCFG_NODES')

    for cls in reversed(classes_misc):
        unregister_class(cls)
    print("\tmisc\t\t" + str(len(classes_misc)))

    for cls in reversed(classes_socket):
        unregister_class(cls)
    print("\tsocket\t\t" + str(len(classes_socket)))

    for cls in reversed(classes_presetnode):
        unregister_class(cls)
    print("\tpreset node\t" + str(len(classes_presetnode)))

    for cls in reversed(classes_node):
        unregister_class(cls)
    print("\tnode\t\t" + str(len(classes_node)))
        
    print("\tproperties")
    del bpy.types.Scene.MCFG_SP_ImportLinkDepth
    del bpy.types.Scene.MCFG_SP_ImportDepth
    del bpy.types.Scene.MCFG_SP_ImportExpressions
    del bpy.types.Scene.MCFG_SP_ExportDir
    del bpy.types.Scene.MCFG_SP_IgnoreErrors
    del bpy.types.Scene.MCFG_SP_OpenFile
    del bpy.types.Scene.MCFG_SP_PresetName
    del bpy.types.Scene.MCFG_SP_PresetDesc
    del bpy.types.Scene.MCFG_SP_ModelSelectionList
    del bpy.types.Scene.MCFG_SP_ModelSelectionListIndex
    del bpy.types.Scene.MCFG_SP_ModelSelectionListListNode
    del bpy.types.Scene.MCFG_SP_PresetList
    del bpy.types.Scene.MCFG_SP_PresetListIndex
    
    del bpy.types.NodeFrame.process_type
    del bpy.types.NodeFrame.doc_url

    print("\tmenus")
    bpy.types.NODE_MT_editor_menus.remove(ui.draw_header)
    bpy.types.TEXT_MT_templates.remove(ui.draw_menu)
    
    print("Unregister done")

if __name__ == "__main__":
    register()