bl_info = {
    "name": "Setup Pixel-Look",
    "blender": (2, 83, 0),
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
from pprint import pprint

class PixelLookSetup(bpy.types.Operator):
    
    bl_idname = "object.cut_to_tiles"
    bl_label = "Setup Pixel-Look"
    bl_options = {'REGISTER', 'UNDO'}
   
    def execute(self, context):  
        
        context = bpy.context

        # Create the set
        unique_materials = set(slot.material for so in context.selected_objects for slot in so.material_slots)
        tree = context.active_object.active_material.node_tree
        links = context.active_object.active_material.node_tree.links

        for mat in unique_materials:
            nodes=mat.node_tree.nodes
            tree = mat.node_tree
            links = tree.links
            
            mat.blend_method = 'CLIP'
            mat.alpha_threshold = 0
            mat.specular_intensity = 0
            
            for node in nodes:                
                if node.type=="BSDF_PRINCIPLED":
                    shader = node
                    
                    node.inputs["Specular"].default_value = 0
                    
                    imageNode = 0
                    for n in links:
                        if n.from_node.type == "TEX_IMAGE":
                            imageNode = n.from_node
                    
                    nodeInput = node.inputs["Alpha"]
                    nodeOutput = imageNode.outputs[0]
                    
                    links.new(
                        nodeOutput,
                        nodeInput
                    )

        for mat in unique_materials:
            nodes = mat.node_tree.nodes
            for node in nodes:
                if node.type=="TEX_IMAGE":
                    node.interpolation="Closest"

        return {'FINISHED'}    


def menu_func(self, context):
    self.layout.operator(PixelLookSetup.bl_idname)

def register():
    bpy.utils.register_class(PixelLookSetup)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(PixelLookSetup)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
