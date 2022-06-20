"""
Find MP to HG(simplified) mapping
"""

import enum
import io
import sys
import numpy as np
from obj_helpers import read_obj, write_obj
from scipy import spatial

def find_nearest(mp_vertices, hg_vertices):

    # We now find the closes for each vertex
    nearest_hg_indexes = []
    for mp_vertex in mp_vertices:

        nearest_hg_index = spatial.KDTree(hg_vertices).query(mp_vertex)[1]
        nearest_hg_indexes.append(nearest_hg_index)
    
    hg_nearest_vertices =  np.take(hg_vertices, nearest_hg_indexes, 0)
    write_obj("nearest.obj", hg_nearest_vertices,  [], [])

    with io.open("mp_to_hg_mapping.txt", "w") as fout:

        for i, mp_vertex in enumerate(mp_vertices):

            fout.write(f"{i} {nearest_hg_indexes[i]}\n")



if __name__ == "__main__":

    mp_vertices, mp_uv, mp_faces, mtl_file_mp, mtl_name_mp = read_obj(sys.argv[1])
    hg_vertices, hg_uv, hg_faces, mtl_file, mtl_name = read_obj(sys.argv[2])

    mp_vertices = np.asarray(mp_vertices)
    hg_vertices = np.asarray(hg_vertices)

    find_nearest(mp_vertices, hg_vertices)