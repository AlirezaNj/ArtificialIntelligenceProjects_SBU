import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Graphics:
    def __init__(self): pass

    def display(self, env):
        #################################
        # fig = plt.figure(figsize=(4,4))
        # ax = fig.add_subplot(111, projection='3d')
        # xs, ys, zs = [], [], []
        # for cube in env.map:
        #     xs.append(cube[0])
        #     ys.append(cube[1])
        #     zs.append(cube[2])

        # ax.scatter(xs,ys,zs)
        # plt.show()
        #################################    
        xs, ys, zs = [], [], []
        for cube in env.map:
            xs.append(cube[0])
            ys.append(cube[1])
            zs.append(cube[2])
        
        max_coordinate = abs(max([max(xs),max(ys),max(zs)]))
        min_coordinate = abs(min([min(xs),min(ys),min(zs)]))
        cube_location = np.zeros((max_coordinate + min_coordinate + 1, max_coordinate + min_coordinate + 1, max_coordinate + min_coordinate + 1))

        for cube in env.map:
            cube_location[cube[0] + min_coordinate, cube[1] + min_coordinate, cube[2] + min_coordinate] = True

        ax = plt.figure().add_subplot(projection='3d')
        ax.set(xlabel='X', ylabel='Y', zlabel='Z')
        ax.voxels(cube_location, edgecolor='k')

        plt.show()