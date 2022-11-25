import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Graphics:
    def __init__(self): pass

    def display(self, env):
        fig = plt.figure(figsize=(4,4))
        ax = fig.add_subplot(111, projection='3d')
        xs, ys, zs = [], [], []
        for cube in env.map:
            xs.append(cube[0])
            ys.append(cube[1])
            zs.append(cube[2])

        ax.scatter(xs,ys,zs)
        plt.show()