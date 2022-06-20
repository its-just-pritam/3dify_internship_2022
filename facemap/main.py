import io
import sys
from matplotlib import pyplot as plt
from obj_helpers import read_obj
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
from scipy.spatial import cKDTree
import math


def nearest_3_points(point, mp_vertices):

    distances = []
    for i in range(len(mp_vertices)):
        dist = math.dist(point, mp_vertices[i])
        distances.append((i, dist))

    distances.sort(key = lambda x: x[1])
    print(distances[0][0], distances[0][1])

    return [distances[0][0], distances[1][0], distances[2][0]]


if __name__ == "__main__":

    mp_vertices, mp_uv, mp_faces, mtl_file_mp, mtl_name_mp = read_obj(sys.argv[1])
    hg_vertices, hg_uv, hg_faces, mtl_file, mtl_name = read_obj(sys.argv[2])

    mp_vertices_2D = [[v[0], v[1]] for v in mp_vertices]
    hg_vertices_2D = [[v[0], v[1]] for v in hg_vertices]

    points = np.array(mp_vertices_2D)
    xs = [x[0] for x in mp_vertices_2D]
    ys = [x[1] for x in mp_vertices_2D]
    plt.scatter(xs, ys)
    plt.show()
    plt.close()
    # vor = Voronoi(points)
    # fig = voronoi_plot_2d(vor)
    # plt.show()
    # plt.close()

    path = 'mp_to_hg_mapping.txt'
    file = open(path,'r')
    str_Array = file.readlines()
    
    for str in str_Array:
        str = str.replace('\n', '')
        str = str.split(' ')
        hg_vertices_2D[int(str[1])] = [None, None]
    file.close()

    hg_points_2_triangles = []
    with io.open("mp_to_hg_mapping_many_2_one.txt", "w") as fout:
        for i in range(len(hg_vertices)):

            if hg_vertices_2D[i][0] != None:
                nearest_points = nearest_3_points(hg_vertices[i], mp_vertices)
                fout.write(f"{i} {nearest_points[0]} {nearest_points[1]} {nearest_points[2]}\n")

    