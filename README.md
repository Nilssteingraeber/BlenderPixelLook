# BlenderPixelLook
A simple Blender addon to make pixelart materials work without changing every material by hand. 
Especially designed to work with exported maps from [DSPRE](https://github.com/AdAstra-LD/DS-Pokemon-Rom-Editor) and [AdAstra's PDSME](https://github.com/AdAstra-LD/Pokemon-DS-Map-Studio) / [Trifindo's PDSME](https://github.com/Trifindo/Pokemon-DS-Map-Studio).


![](https://github.com/Nilssteingraeber/BlenderPixelLook/blob/main/GithubPixelateAnimation.gif)

## What it does

The addon changes every material of the selected object:
1. Setting interpolation mode to "nearest neighbor" / "closest"
2. Setting correct alpha textures
3. Setting blending mode to "alpha clip" / "clip" 

## How to install

Blender Version 4.0 - 2.83:

1. Download the Python script corresponding with the Blender version you are working with.
2. In Blender, go to Edit -> Preferences -> Add-ons
3. Click on "Install..." and select the downloaded .py file.
4. Click on the checkbox to enable it

___

After clicking the checkbox, you should the something along those lines:

![](https://github.com/Nilssteingraeber/BlenderPixelLook/blob/main/InstallPromptGithub.png) 
