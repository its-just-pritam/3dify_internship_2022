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
    
    # Import the source object
    src_FBXfilePath = 'C:/Users/srita/Desktop/3dify_internship/facemap/mp_face_temp_scaled.obj'
    mp_obj = bpy.ops.import_scene.obj(filepath=src_FBXfilePath, split_mode='OFF')
    mp_name = bpy.context.scene.objects[0].name
    
    # Import the target object
    tar_FBXfilePath = 'C:/Users/srita/Desktop/3dify_internship/facemap/face_2.obj'
    _obj = bpy.ops.import_scene.obj(filepath=tar_FBXfilePath, split_mode='OFF')
    _name = bpy.context.scene.objects[1].name
    
    path = 'C:\\Users\\srita\Desktop\\3dify_internship\\facemap\\mp_to_hg_mapping_many_2_one.txt'
    file = open(path,'r')
    str_Array = file.readlines()
    many_one_map = []
    
    for str in str_Array:
        str = str.replace('\n', '')
        str = str.split(' ')
        many_one_map.append([int(str[0]), int(str[1]), int(str[2]), int(str[3])])
    file.close()
        
    mp_obj = bpy.context.scene.objects[mp_name]
    _obj = bpy.context.scene.objects[_name]
    
    selectObject([mp_name])
    mp_co = [i.co for i in bpy.context.active_object.data.vertices if i.select]
    
    selectObject([_name])

    for map in many_one_map:

        _v = bpy.context.active_object.data.vertices[map[0]].co
        P1 = mp_co[map[1]]
        P2 = mp_co[map[2]]
        P3 = mp_co[map[3]]
        projected = find_projection(_v, [P1, P2, P3])
        print(_v, projected)
        bpy.context.active_object.data.vertices[map[0]].co = (projected[0], projected[1], projected[2])
        
    
    export_path = 'C:/Users/srita/Desktop/3dify_internship/facemap/template.obj'
    bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)