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
    bl_idname = "object.setup_pixel_look"
    bl_label = "Setup Pixel Look"
    bl_options = {'REGISTER', 'UNDO'}

    total: bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

   
    def execute(self, context):  
          
        return {'FINISHED'}    


def menu_func(self, context):
    self.layout.operator(PixelLookSetup.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []


def register():
    bpy.utils.register_class(PixelLookSetup)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(PixelLookSetup)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
