bl_info = {
    "name": "Arma 3 model.cfg node editor",
    "author": "MrClock",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "Model config editor",
    "description": "Node tree based tool for creating model configuration files",
    # "warning": "Work in progress",
    # "tracket_url": "",
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
    importlib.reload(nodes.n_inspect)
    importlib.reload(nodes.n_joinList)
    importlib.reload(nodes.n_mathBasic)
    importlib.reload(nodes.n_model)
    importlib.reload(nodes.n_section)
    importlib.reload(nodes.n_sectionList)
    importlib.reload(nodes.n_skeleton)
    importlib.reload(nodes.n_valueFloat)
    importlib.reload(nodes.n_valueString)
    
    # Node presets
    importlib.reload(nodepresets.n_animationListPresetBullets)
    importlib.reload(nodepresets.n_animationPresetMagazine)
    importlib.reload(nodepresets.n_animationPresetMuzzleflash)
    importlib.reload(nodepresets.n_animationPresetSelector)
    importlib.reload(nodepresets.n_animationPresetSight)
    importlib.reload(nodepresets.n_animationPresetTrigger)
    importlib.reload(nodepresets.n_boneListPresetGenerate)
    importlib.reload(nodepresets.n_boneListPresetReplace)
    importlib.reload(nodepresets.n_boneListPresetStandards)
    importlib.reload(nodepresets.n_boneListPresetSymmetrize)
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
    importlib.reload(sockets.s_skeletonIsDiscrete)
    importlib.reload(sockets.s_skeletonParent)
    importlib.reload(sockets.s_universal)
    importlib.reload(sockets.s_valueFloat)
    importlib.reload(sockets.s_valueString)
    
    # Misc
    importlib.reload(n_tree)
    importlib.reload(ui)
    importlib.reload(utility)
    importlib.reload(utility_data)
    importlib.reload(utility_presets)
    importlib.reload(utility_presets_setup)

else:
    # Nodes
    from . nodes import n_animation
    from . nodes import n_animationList
    from . nodes import n_bone
    from . nodes import n_boneList
    from . nodes import n_inspect
    from . nodes import n_joinList
    from . nodes import n_mathBasic
    from . nodes import n_model
    from . nodes import n_section
    from . nodes import n_sectionList
    from . nodes import n_skeleton
    from . nodes import n_valueFloat
    from . nodes import n_valueString
    
    # Node presets
    from . nodepresets import n_animationListPresetBullets
    from . nodepresets import n_animationPresetMagazine
    from . nodepresets import n_animationPresetMuzzleflash
    from . nodepresets import n_animationPresetSelector
    from . nodepresets import n_animationPresetSight
    from . nodepresets import n_animationPresetTrigger
    from . nodepresets import n_boneListPresetGenerate
    from . nodepresets import n_boneListPresetReplace
    from . nodepresets import n_boneListPresetStandards
    from . nodepresets import n_boneListPresetSymmetrize
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
    from . sockets import s_skeletonIsDiscrete
    from . sockets import s_skeletonParent
    from . sockets import s_universal
    from . sockets import s_valueFloat
    from . sockets import s_valueString
    
    # Misc
    from . import n_tree
    from . import ui
    from . import utility
    from . import utility_data
    from . import utility_presets
    from . import utility_presets_setup

import bpy
import os

# Addon preferences
class MCFG_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    
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
        name = "Operator",
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
            ('CONSOLE',"System console","Output the log to Blender's system console"),
            ('FILE',"Log file","Output the log to a .log text file in the export directory")
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
        description="Folder that contains the .py files describing custom setup presets", 
        subtype='DIR_PATH',
        default=""
    )
    
    def draw(self,context):
        layout = self.layout
        
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Color settings")
        col.prop(self,"useCustomColors")
        if self.useCustomColors:
            row = box.row()
            row.prop(self,"customColorSkeleton")
            row.prop(self,"customColorBones")
            row.prop(self,"customColorModel")
            row = box.row()
            row.prop(self,"customColorSection")
            row.prop(self,"customColorAnimations")
            row.prop(self,"customColorOperator")
            
        box = layout.box()
        box.label(text="Validation settings")
        row = box.row()
        row.prop(self,"warnsAreErr")
        box.prop(self,"validationOutput")
        
        box = layout.box()
        box.label(text="Preset settings")
        box.prop(self,"customSetupPresets")
        
import nodeitems_utils
from nodeitems_utils import NodeItem

# node menu
node_categories = [
    n_tree.MCFG_N_Category('SKELETONNODES', "Skeleton", items=[
        NodeItem("MCFG_N_Skeleton")
    ]),
    n_tree.MCFG_N_Category('SKELETONPRESETNODES', "Skeleton presets", items=[
        NodeItem("MCFG_N_SkeletonPresetDefault"),
        NodeItem("MCFG_N_SkeletonPresetArmaman")
    ]),
    n_tree.MCFG_N_Category('MODELNODES', "Model", items=[
        NodeItem("MCFG_N_Model")
    ]),
    n_tree.MCFG_N_Category('MODELPRESETNODES', "Model presets", items=[
        NodeItem("MCFG_N_ModelPresetDefault"),
        NodeItem("MCFG_N_ModelPresetCopy"),
        NodeItem("MCFG_N_ModelPresetArmaman")
    ]),
    n_tree.MCFG_N_Category('BONENODES', "Bone", items=[
        NodeItem("MCFG_N_Bone"),
        NodeItem("MCFG_N_BoneList")
    ]),
    n_tree.MCFG_N_Category('BONEPRESETNODES', "Bone presets", items=[
        NodeItem("MCFG_N_BoneListPresetStandardWeapon"),
        NodeItem("MCFG_N_BoneListPresetGenerate"),
        NodeItem("MCFG_N_BoneListPresetReplace"),
        NodeItem("MCFG_N_BoneListPresetSymmetrize")
    ]),
    n_tree.MCFG_N_Category('SECTIONNODES', "Section", items=[
        NodeItem("MCFG_N_Section"),
        NodeItem("MCFG_N_SectionList")
    ]),
    n_tree.MCFG_N_Category('ANIMATIONNODES', "Animation", items=[
        NodeItem("MCFG_N_AnimationTranslation"),
        NodeItem("MCFG_N_AnimationTranslationX"),
        NodeItem("MCFG_N_AnimationTranslationY"),
        NodeItem("MCFG_N_AnimationTranslationZ"),
        NodeItem("MCFG_N_AnimationRotation"),
        NodeItem("MCFG_N_AnimationRotationX"),
        NodeItem("MCFG_N_AnimationRotationY"),
        NodeItem("MCFG_N_AnimationRotationZ"),
        NodeItem("MCFG_N_AnimationHide"),
        NodeItem("MCFG_N_AnimationList")
    ]),
    n_tree.MCFG_N_Category('ANIMATIONPRESETNODES', "Animation presets", items=[
        NodeItem("MCFG_N_AnimationPresetMuzzleflashRot"),
        NodeItem("MCFG_N_AnimationPresetTriggerRot"),
        NodeItem("MCFG_N_AnimationPresetTriggerMove"),
        NodeItem("MCFG_N_AnimationPresetSelectorRot"),
        NodeItem("MCFG_N_AnimationPresetSightHide"),
        NodeItem("MCFG_N_AnimationPresetMagazineHide"),
        NodeItem("MCFG_N_AnimationListPresetBulletsHide")
    ]),
    n_tree.MCFG_N_Category('OPERATORS', "Operators", items=[
        NodeItem("MCFG_N_JoinList"),
        NodeItem("MCFG_N_ValueFloat"),
        NodeItem("MCFG_N_ValueString"),
        NodeItem("MCFG_N_MathBasic"),
        NodeItem("MCFG_N_Inspect")
    ]),
    n_tree.MCFG_N_Category('LAYOUTNODES', "Layout", items=[
        NodeItem("NodeFrame")
    ])
]

# Registration

classes = (
    
    # Nodes
    nodes.n_animation.MCFG_N_AnimationTranslation,
    nodes.n_animation.MCFG_N_AnimationTranslationX,
    nodes.n_animation.MCFG_N_AnimationTranslationY,
    nodes.n_animation.MCFG_N_AnimationTranslationZ,
    nodes.n_animation.MCFG_N_AnimationRotation,
    nodes.n_animation.MCFG_N_AnimationRotationX,
    nodes.n_animation.MCFG_N_AnimationRotationY,
    nodes.n_animation.MCFG_N_AnimationRotationZ,
    nodes.n_animation.MCFG_N_AnimationHide,
    nodes.n_animationList.MCFG_N_AnimationList,
    nodes.n_bone.MCFG_N_Bone,
    nodes.n_boneList.MCFG_N_BoneList,
    nodes.n_inspect.MCFG_N_Inspect,
    nodes.n_joinList.MCFG_N_JoinList,
    nodes.n_mathBasic.MCFG_N_MathBasic,
    nodes.n_model.MCFG_N_Model,
    nodes.n_section.MCFG_N_Section,
    nodes.n_sectionList.MCFG_N_SectionList,
    nodes.n_skeleton.MCFG_N_Skeleton,
    nodes.n_valueFloat.MCFG_N_ValueFloat,
    nodes.n_valueString.MCFG_N_ValueString,
    
    # Node presets
    nodepresets.n_animationListPresetBullets.MCFG_N_AnimationListPresetBulletsHide,
    nodepresets.n_animationPresetMagazine.MCFG_N_AnimationPresetMagazineHide,
    nodepresets.n_animationPresetMuzzleflash.MCFG_N_AnimationPresetMuzzleflashRot,
    nodepresets.n_animationPresetSelector.MCFG_N_AnimationPresetSelectorRot,
    nodepresets.n_animationPresetSight.MCFG_N_AnimationPresetSightHide,
    nodepresets.n_animationPresetTrigger.MCFG_N_AnimationPresetTriggerRot,
    nodepresets.n_animationPresetTrigger.MCFG_N_AnimationPresetTriggerMove,
    nodepresets.n_boneListPresetGenerate.MCFG_N_BoneListPresetGenerate,
    nodepresets.n_boneListPresetReplace.MCFG_N_BoneListPresetReplace,
    nodepresets.n_boneListPresetStandards.MCFG_N_BoneListPresetStandardWeapon,
    nodepresets.n_boneListPresetSymmetrize.MCFG_N_BoneListPresetSymmetrize,
    nodepresets.n_modelPresetArmaman.MCFG_N_ModelPresetArmaman,
    nodepresets.n_modelPresetCopy.MCFG_N_ModelPresetCopy,
    nodepresets.n_modelPresetDefault.MCFG_N_ModelPresetDefault,
    nodepresets.n_skeletonPresetArmaman.MCFG_N_SkeletonPresetArmaman,
    nodepresets.n_skeletonPresetDefault.MCFG_N_SkeletonPresetDefault,
    
    # Sockets
    sockets.s_list.MCFG_S_List,
    sockets.s_modelAnimation.MCFG_S_ModelAnimation,
    sockets.s_modelAnimationList.MCFG_S_ModelAnimationList,
    sockets.s_modelParent.MCFG_S_ModelParent,
    sockets.s_modelSection.MCFG_S_ModelSection,
    sockets.s_modelSectionList.MCFG_S_ModelSectionList,
    sockets.s_modelSourceAddress.MCFG_S_ModelSourceAddress,
    sockets.s_skeletonBone.MCFG_S_SkeletonBone,
    sockets.s_skeletonBoneList.MCFG_S_SkeletonBoneList,
    sockets.s_skeletonIsDiscrete.MCFG_S_SkeletonIsDiscrete,
    sockets.s_skeletonParent.MCFG_S_SkeletonParent,
    sockets.s_universal.MCFG_S_Universal,
    sockets.s_valueFloat.MCFG_S_ValueFloat,
    sockets.s_valueString.MCFG_S_ValueString,
    
    # Misc
    MCFG_Preferences,
    n_tree.MCFG_N_Tree,
    n_tree.MCFG_N_Frame,
    ui.MCFG_ReportBox,
    ui.MCFG_Panel_Export,
    ui.MCFG_Panel_Validate,
    ui.MCFG_Panel_AddPreset,
    ui.MCFG_Panel_Inspect,
    ui.MCFG_PT_Panel_Inspect,
    ui.MCFG_PT_Panel_Export,
    ui.MCFG_PT_Panel_Presets,
    ui.MCFG_PT_Panel_Docs
)

def register():
    print("Model Cfg editor registering")
    print(__name__)
    from bpy.utils import register_class
    for cls in classes:
        print(cls)
        register_class(cls)

    nodeitems_utils.register_node_categories('MODELCFG_NODES', node_categories)
    
    bpy.types.Scene.modelCfgExportDir = bpy.props.StringProperty (
        name = "Directory",
        description = "Directory to save file to",
        default = "",
        subtype = 'DIR_PATH'
    )
    bpy.types.Scene.modelCfgEditorSetupPresets = bpy.props.EnumProperty (
        name = "",
        description = "Node setup presets",
        default = None,
        items = utility_presets_setup.GetSetups
    )
    bpy.types.Scene.modelCfgEditorIgnoreErrors = bpy.props.BoolProperty (
        name = "Ignore errors",
        description = "(NOT RECOMMENDED) Export setup regardless of whether or not the validation succeeds",
        default = False
    )
    
    bpy.types.NODE_MT_editor_menus.append(ui.draw_header)
    
    print("Register done")

def unregister():
    nodeitems_utils.unregister_node_categories('MODELCFG_NODES')

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
    del bpy.types.Scene.modelCfgExportDir
    del bpy.types.Scene.modelCfgEditorSetupPresets

    bpy.types.NODE_MT_editor_menus.remove(ui.draw_header)

if __name__ == "__main__":
    register()