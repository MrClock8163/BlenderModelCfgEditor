# Arma 3 model.cfg editor for Blender

The goal of this project is to provide a visual, intuitive way to create the required model.cfg files for models intended for import to the game Arma 3.
The project is still heavily in development, new features are still to be added.

# How does it work?

This Blender addon introduces an entirely new node editor workplace to Blender called **Model Config Editor**. This interface makes it possible to create model.cfg setups through a node-based workflow. The classes and properties (eg.: skeletons, model, animations etc.) of a traditional model configuration file are represented by a variety of nodes, node settings. The available nodes beside the basic ones also include some handy preset generators for frequently needed operation, such as a bone structure symmetrizer, different animation generators, standard Arma 3 skeleton and model presets (eg.: for OFP2_ManSkeleton and ArmaMan) and much more.

Once the setup is completed the structure can be validated and exported to the selected folder. During export, the nodes are processed and the result is printed out into the appripriate file.
