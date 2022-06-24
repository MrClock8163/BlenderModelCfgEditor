# Arma 3 model.cfg editor for Blender

<p align="center">
    <img src="https://user-images.githubusercontent.com/48679831/174893537-f5ff49de-2058-43af-86f6-4a888ad16f82.png" width="200">
</p>

The goal of this project is to provide a visual and intuitive way to create the required model.cfg files for models intended for import to the Arma 3 game.
The project is still heavily in development, new features are still to be added.

## How does it work?

This Blender addon introduces an entirely new node editor workplace to Blender called **Model Config Editor**. This interface makes it possible to create model.cfg setups through a node-based workflow. The classes and properties (eg.: skeletons, model, animations etc.) of a traditional model configuration file are represented by a variety of nodes, node settings. The available nodes beside the basic ones also include some handy preset generators for frequently needed operations (such as a bone structure symmetrizer), different animation generators, standard Arma 3 skeleton and model presets (eg.: for OFP2_ManSkeleton and ArmaMan) and much more.

Once the setup is completed, the structure can be validated and exported to the selected folder. During export, the nodes are processed and the result is printed out into the appropriate file.

## Key features
- Visual representation of configuration setups
  - Generic nodes for configurations
  - Preset nodes for freqently needed components
  - Custom scripted nodes for special cases
- Creation of sections and bones from existing model selections
- Raw node data inspection
- Node setup presets
  - Built-in
  - Custom
- Output validation
- Export to model.cfg format
- Ability to store setup data in editable format in BLEND file

## Benefits
- Eliminates the chance of making typos or forgetting necessary properties
- Allows for both special setups through universal nodes, and frequent, standardized setups through preset nodes
- Speeds up the creation of frequent configurations
- Allows to have every part of the import work be done in Blender

## Disclaimer and documentation
### Disclaimer
While this project seeks to eliminate the need for manual (as in typing it by hand) creation of model.cfg files, knowledge of their structure, capabilities and limitaions is still necessary to utilize this addon. Some basic (although granted, not at all thorough) information about them can be found on the [Arma 3 Community Wiki](https://community.bistudio.com/wiki/Model_Config). It is also worth nothing that the main purpose of this addon is to speed up the creation of relatively simple configurations, complex configs will still take a long time (so do not expect this addon to be the Messiah, the solver of all problems).

The concept of this project was mostly inspired by the [Rigging nodes](https://gitlab.com/AquaticNightmare/rigging_nodes/-/releases) addon by AquaticNightmare but no actual code was taken from the project.

The programming of this addon is most likely not the best, or most efficient, but it functions, and it is not performance heavy as code only really runs during validation and export. Part of the reason for this is that there is very little documentation for custom node editors in Blender, so most of the development consists of trial-error. Please keep this in mind.

The addon is most useful in Blender based workflows, and used in conjunction with Alwarren's [Arma Toolbox](https://github.com/AlwarrenSidh/ArmAToolbox) specifically, thus allowing to have the entire process from modelling to importing be done entirely in Blender.

### Documentation
The documentation of this addon is still underway, it will be available in the [wiki](https://github.com/MrClock8163/BlenderModelCfgEditor/wiki) section of the GitHub repository.

## Requirements
This Blender addon requires v2.83.0 of Blender or higher, as previous versions do not support custom node editor workspaces.

## Contact
I'm available on Discord by the name MrClock#8163. You can find me on the [Just Like The Simulations | Arma 3 mods](https://discord.gg/KQSBDF3) Discord server.
