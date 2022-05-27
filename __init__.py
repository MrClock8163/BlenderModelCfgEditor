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
    "doc_url": "https://discord.gg/KQSBDF3",
    "category": "Node"
}

if "bpy" in locals():
    import importlib
    importlib.reload(n_tree)
    importlib.reload(s_skeletonParent)
    # importlib.reload(s_skeletonOutput)
    importlib.reload(s_skeletonBone)
    importlib.reload(s_skeletonBoneList)
    importlib.reload(s_skeletonIsDiscrete)
    importlib.reload(n_skeleton)
    importlib.reload(n_skeletonPresetDefault)
    importlib.reload(n_skeletonPresetArmaman)
    importlib.reload(n_bone)
    importlib.reload(n_boneList)
    importlib.reload(n_boneListPresetGenerate)
    importlib.reload(n_boneListPresetStandards)
    importlib.reload(n_boneListPresetReplace)
    importlib.reload(n_boneListPresetSymmetrize)
    importlib.reload(n_model)
    importlib.reload(n_modelPresetDefault)
    importlib.reload(n_modelPresetCopy)
    importlib.reload(n_modelPresetArmaman)
    importlib.reload(s_list)
    importlib.reload(n_joinList)
    importlib.reload(s_modelParent)
    importlib.reload(s_modelSection)
    importlib.reload(s_modelSectionList)
    importlib.reload(s_modelAnimation)
    importlib.reload(s_modelAnimationList)
    importlib.reload(n_section)
    importlib.reload(n_sectionList)
    importlib.reload(n_animation)
    importlib.reload(n_animationPresetMuzzleflash)
    importlib.reload(n_animationPresetTrigger)
    importlib.reload(n_animationPresetSelector)
    importlib.reload(n_animationPresetSight)
    importlib.reload(n_animationPresetMagazine)
    importlib.reload(n_animationList)
    importlib.reload(n_animationListPresetBullets)
    importlib.reload(s_valueFloat)
    importlib.reload(n_valueFloat)
    importlib.reload(s_valueString)
    importlib.reload(n_valueString)
    importlib.reload(s_modelSourceAddress)
    importlib.reload(ui)
    importlib.reload(utility)
    importlib.reload(utility_data)
    importlib.reload(utility_presets)

else:
    from . import n_tree
    from . import s_skeletonParent
    # from . import s_skeletonOutput
    from . import s_skeletonBone
    from . import s_skeletonBoneList
    from . import s_skeletonIsDiscrete
    from . import n_skeleton
    from . import n_skeletonPresetDefault
    from . import n_skeletonPresetArmaman
    from . import n_bone
    from . import n_boneList
    from . import n_boneListPresetGenerate
    from . import n_boneListPresetStandards
    from . import n_boneListPresetReplace
    from . import n_boneListPresetSymmetrize
    from . import n_model
    from . import n_modelPresetDefault
    from . import n_modelPresetCopy
    from . import n_modelPresetArmaman
    from . import s_list
    from . import n_joinList
    from . import s_modelParent
    from . import s_modelSection
    from . import s_modelSectionList
    from . import s_modelAnimation
    from . import s_modelAnimationList
    from . import n_section
    from . import n_sectionList
    from . import n_animation
    from . import n_animationPresetMuzzleflash
    from . import n_animationPresetTrigger
    from . import n_animationPresetSelector
    from . import n_animationPresetSight
    from . import n_animationPresetMagazine
    from . import n_animationList
    from . import n_animationListPresetBullets
    from . import s_valueFloat
    from . import n_valueFloat
    from . import s_valueString
    from . import n_valueString
    from . import s_modelSourceAddress
    from . import ui
    from . import utility
    from . import utility_data
    from . import utility_presets

import bpy
import os

# Addon preferences
class MCFG_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    
    # Color settings
    useCustomColors: bpy.props.BoolProperty(
        description = "Display nodes belonging to the distinct categories with unique background colors.",
        name = "Use custom node colors",
        default = False
    )
    customColorSkeleton: bpy.props.FloatVectorProperty(
        name = "Skeleton nodes",
        description = "Color used for skeleton related nodes",
        subtype = 'COLOR',
        default = (0.792, 0.322, 0.067),
        min = 0.0,
        max = 1.0
    )
    customColorModel: bpy.props.FloatVectorProperty(
        name = "Model nodes",
        description = "Color used for model related nodes",
        subtype = 'COLOR',
        default = (0.0, 1.0, 1.0),
        min = 0.0,
        max = 1.0
    )
    customColorBones: bpy.props.FloatVectorProperty(
        name = "Bone nodes",
        description = "Color used for bone related nodes",
        subtype = 'COLOR',
        default = (0.902, 0.271,0.333),
        min = 0.0,
        max = 1.0
    )
    customColorAnimations: bpy.props.FloatVectorProperty(
        name = "Animation nodes",
        description = "Color used for animation related nodes",
        subtype = 'COLOR',
        default = (0.239, 0.741,0.996),
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
    
    def draw(self,context):
        layout = self.layout
        
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Color settings")
        col.prop(self,"useCustomColors")
        if self.useCustomColors:
            col.prop(self,"customColorSkeleton")
            col.prop(self,"customColorModel")
            col.prop(self,"customColorBones")
            col.prop(self,"customColorAnimations")
            
        box = layout.box()
        box.label(text="Validation settings")
        row = box.row()
        row.prop(self,"warnsAreErr")
        box.prop(self,"validationOutput")
        
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
        NodeItem("MCFG_N_ValueFloat"),
        NodeItem("MCFG_N_ValueString"),
        NodeItem("MCFG_N_JoinList")
    ]),
    n_tree.MCFG_N_Category('LAYOUTNODES', "Layout", items=[
        NodeItem("NodeFrame")
    ])
]

# Registration

classes = (
    MCFG_Preferences,
    n_tree.MCFG_N_Tree,
    n_tree.MCFG_N_Frame,
    s_skeletonParent.MCFG_S_SkeletonParent,
    # s_skeletonOutput.MCFG_S_SkeletonOutput,
    s_skeletonBone.MCFG_S_SkeletonBone,
    s_skeletonBoneList.MCFG_S_SkeletonBoneList,
    s_skeletonIsDiscrete.MCFG_S_SkeletonIsDiscrete,
    n_skeleton.MCFG_N_Skeleton,
    n_skeletonPresetDefault.MCFG_N_SkeletonPresetDefault,
    n_skeletonPresetArmaman.MCFG_N_SkeletonPresetArmaman,
    n_bone.MCFG_N_Bone,
    n_boneList.MCFG_N_BoneList,
    n_boneListPresetGenerate.MCFG_N_BoneListPresetGenerate,
    n_boneListPresetStandards.MCFG_N_BoneListPresetStandardWeapon,
    n_boneListPresetReplace.MCFG_N_BoneListPresetReplace,
    n_boneListPresetSymmetrize.MCFG_N_BoneListPresetSymmetrize,
    n_model.MCFG_N_Model,
    n_modelPresetDefault.MCFG_N_ModelPresetDefault,
    n_modelPresetCopy.MCFG_N_ModelPresetCopy,
    n_modelPresetArmaman.MCFG_N_ModelPresetArmaman,
    s_list.MCFG_S_List,
    n_joinList.MCFG_N_JoinList,
    s_modelParent.MCFG_S_ModelParent,
    s_modelSection.MCFG_S_ModelSection,
    s_modelSectionList.MCFG_S_ModelSectionList,
    s_modelAnimation.MCFG_S_ModelAnimation,
    s_modelAnimationList.MCFG_S_ModelAnimationList,
    n_section.MCFG_N_Section,
    n_sectionList.MCFG_N_SectionList,
    n_animation.MCFG_N_AnimationTranslation,
    n_animation.MCFG_N_AnimationTranslationX,
    n_animation.MCFG_N_AnimationTranslationY,
    n_animation.MCFG_N_AnimationTranslationZ,
    n_animation.MCFG_N_AnimationRotation,
    n_animation.MCFG_N_AnimationRotationX,
    n_animation.MCFG_N_AnimationRotationY,
    n_animation.MCFG_N_AnimationRotationZ,
    n_animation.MCFG_N_AnimationHide,
    n_animationPresetMuzzleflash.MCFG_N_AnimationPresetMuzzleflashRot,
    n_animationPresetTrigger.MCFG_N_AnimationPresetTriggerRot,
    n_animationPresetTrigger.MCFG_N_AnimationPresetTriggerMove,
    n_animationPresetSelector.MCFG_N_AnimationPresetSelectorRot,
    n_animationPresetSight.MCFG_N_AnimationPresetSightHide,
    n_animationPresetMagazine.MCFG_N_AnimationPresetMagazineHide,
    n_animationList.MCFG_N_AnimationList,
    n_animationListPresetBullets.MCFG_N_AnimationListPresetBulletsHide,
    s_valueFloat.MCFG_S_ValueFloat,
    n_valueFloat.MCFG_N_ValueFloat,
    s_valueString.MCFG_S_ValueString,
    n_valueString.MCFG_N_ValueString,
    s_modelSourceAddress.MCFG_S_ModelSourceAddress,
    # ui.MCFG_InfoBox,
    ui.MCFG_ReportBox,
    ui.MCFG_Panel_Export,
    ui.MCFG_Panel_Validate,
    ui.MCFG_PT_Panel
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
    
    bpy.types.NODE_MT_editor_menus.append(ui.draw_header)
    
    print("Register done")

def unregister():
    nodeitems_utils.unregister_node_categories('MODELCFG_NODES')

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
    del bpy.types.Scene.modelCfgExportDir

    bpy.types.NODE_MT_editor_menus.remove(ui.draw_header)

if __name__ == "__main__":
    register()