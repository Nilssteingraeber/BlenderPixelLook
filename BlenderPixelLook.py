 bl_info = {
    "name": "Setup Pixel-Look",
    "blender": (4, 0, 0),
    "category": "Object",
}

import bpy, bmesh
from bpy import context
from  mathutils import Vector
import math
import numpy
from collections import defaultdict
import sys
import time
from random import random


class PixelLookSetup(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "object.cut_to_tiles"
    bl_label = "Cut Tiles"
    bl_options = {'REGISTER', 'UNDO'}

    total: bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

   
    def execute(self, context):  
          
        return {'FINISHED'}    


def menu_func(self, context):
    self.layout.operator(CutToTiles.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []


def register():
    bpy.utils.register_class(PixelLookSetup)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    # Note: when unregistering, it's usually good practice to do it in reverse order you registered.
    # Can avoid strange issues like keymap still referring to operators already unregistered...
    # handle the keymap

    bpy.utils.unregister_class(PixelLookSetup)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()