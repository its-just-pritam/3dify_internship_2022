import math
import numpy as np
import bpy
import os
import sys
import mathutils


def selectObject(names):
        
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    
    for name in names:
        # Get the object
        ob = bpy.context.scene.objects[name]
    
        # Make the target the active object 
        bpy.context.view_layer.objects.active = ob
    
        # Select the target object
        ob.select_set(True)
        

def find_projection(point, triangle):

    P3_P1 = triangle[2] - triangle[0]
    P2_P1 = triangle[1] - triangle[0]
    P_P1 = point - triangle[0]

    normal = np.cross(P3_P1, P2_P1)
    normal_proj = np.dot(P_P1, normal) * normal / (normal.dot(normal))
    normal_proj = mathutils.Vector((normal_proj[0], normal_proj[1], normal_proj[2]))

    XYZ = point - normal_proj
    print(point, normal_proj)
    print(math.dist(point, XYZ))

    return XYZ


if __name__=="__main__":
    
    # Select and delete all objects to start with a clean space
 
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)
    
    # Import the reference object
    ref_OBJfilePath = 'C:/Users/srita/Desktop/3dify_internship/facemap_next/face_smile.obj'
    ref_obj = bpy.ops.import_scene.obj(filepath=ref_OBJfilePath, split_mode='OFF')
    ref_name = bpy.context.scene.objects[0].name
    ref_obj = bpy.context.scene.objects[ref_name]
    print(ref_name)
    
    
    # Import the mould object
    mould_OBJfilePath = 'C:/Users/srita/Desktop/3dify_internship/facemap_next/input_mp_face.obj'
    mould_obj = bpy.ops.import_scene.obj(filepath=mould_OBJfilePath, split_mode='OFF')
    mould_name = bpy.context.scene.objects[1].name
    mould_obj = bpy.context.scene.objects[mould_name]
    print(mould_name)

    # Import the template object
    temp_OBJfilePath = 'C:/Users/srita/Desktop/3dify_internship/facemap_next/template.obj'
    temp_obj = bpy.ops.import_scene.obj(filepath=temp_OBJfilePath, split_mode='OFF')
    temp_name = bpy.context.scene.objects[2].name
    temp_obj = bpy.context.scene.objects[temp_name]
    print(temp_name)
    
    selectObject([mould_name, ref_name, temp_name])
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    old_loc = [mould_obj.location[0], mould_obj.location[1], mould_obj.location[2]]
    mould_obj.location = ref_obj.location
    temp_obj.location[0] += mould_obj.location[0] - old_loc[0]
    temp_obj.location[1] += mould_obj.location[1] - old_loc[1]
    temp_obj.location[2] += mould_obj.location[2] - old_loc[2]
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)


#    export_path = 'C:/Users/srita/Desktop/3dify_internship/facemap_next/template.obj'
#    bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)