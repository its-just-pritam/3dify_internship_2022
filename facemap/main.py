import io
import re
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
    return [distances[0][0], distances[1][0], distances[2][0]]


def nearest_face(point, centroids):

    distances = []
    for i in range(len(centroids)):
        dist = math.dist(point, centroids[i])
        distances.append((i, dist))

    distances.sort(key = lambda x: x[1])
    return distances[0][0]


def find_centroids(vertices, faces):

    centroids = []
    for item in faces:
        # print(item[0])
        # print(vertices[item[0][0]-1][0], vertices[item[0][1]-1][0], vertices[item[0][2]-1][0])
        P1 = (vertices[item[0][0]-1][0] + vertices[item[0][1]-1][0] + vertices[item[0][2]-1][0]) / 3
        P2 = (vertices[item[0][0]-1][1] + vertices[item[0][1]-1][1] + vertices[item[0][2]-1][1]) / 3
        P3 = (vertices[item[0][0]-1][2] + vertices[item[0][1]-1][2] + vertices[item[0][2]-1][2]) / 3
        centroids.append([P1, P2, P3])
    
    return centroids


if __name__ == "__main__":

    mp_vertices, mp_uv, mp_faces, mtl_file_mp, mtl_name_mp = read_obj(sys.argv[1])
    hg_vertices, hg_uv, hg_faces, mtl_file, mtl_name = read_obj(sys.argv[2])
    # print(mp_vertices)

    mp_vertices_2D = [[v[0], v[1]] for v in mp_vertices]
    hg_vertices_2D = [[v[0], v[1]] for v in hg_vertices]

    points = np.array(mp_vertices_2D)
    xs = [x[0] for x in mp_vertices_2D]
    ys = [x[1] for x in mp_vertices_2D]
    plt.scatter(xs, ys)
    plt.show()
    plt.close()

    path = 'vert_ignore.txt'
    file = open(path,'r')
    str_Array = file.readlines()

    for str in str_Array:
        str = str.replace('\n', '')
        str = str.split(' ')
        hg_vertices_2D[int(str[0])] = [None, None]
    file.close()

    centroids = find_centroids(mp_vertices, mp_faces)
    with io.open("mp_to_hg_mapping_many_2_one.txt", "w") as fout:
        for i in range(len(hg_vertices)):

            if hg_vertices_2D[i][0] != None:
                nearest_tri = nearest_face(hg_vertices[i], centroids)
                print(i, mp_faces[nearest_tri][0][0], mp_faces[nearest_tri][0][1], mp_faces[nearest_tri][0][2])
                fout.write(f"{i} {mp_faces[nearest_tri][0][0]-1} {mp_faces[nearest_tri][0][1]-1} {mp_faces[nearest_tri][0][2]-1}\n")
        
            # nearest_tri = nearest_face(hg_vertices[i], centroids)
            # print(i, mp_faces[nearest_tri][0][0], mp_faces[nearest_tri][0][1], mp_faces[nearest_tri][0][2])
            # fout.write(f"{i} {mp_faces[nearest_tri][0][0]-1} {mp_faces[nearest_tri][0][1]-1} {mp_faces[nearest_tri][0][2]-1}\n")
