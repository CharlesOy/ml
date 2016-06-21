# -*- coding: utf-8 -*-
"""
this Python script is for displaying k nearest neighbors algorithm.
"""
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def generate_points(group_number=2, edge_length=0.2, point_number=10):
    """
    generating some groups of points and draw them
    :param group_number: number of groups
    :param edge_length: every group of points will distributes in a small cube,
    edge_length is the edge length of the cube
    :param point_number: number of points
    :return: location of the random points
    """
    # group_number should in [1, 5]
    group_number = int(round(group_number))
    if group_number > 5 or group_number < 1:
        group_number = 2
    # edge_length should in [0.1, 0.5]
    if edge_length > 0.55 or edge_length < 0.1:
        edge_length = 0.2
    # point_number should in [1,20]
    point_number = int(round(point_number))
    if point_number < 1 or point_number > 20:
        point_number = 10

    # colors
    colors = ('red', 'green', 'blue', 'black', 'grey')
    dots = []
    for i in range(group_number):
        # get random points
        x = np.random.sample(point_number) * edge_length + np.random.random() * (1 - edge_length)
        y = np.random.sample(point_number) * edge_length + np.random.random() * (1 - edge_length)
        z = np.random.sample(point_number) * edge_length + np.random.random() * (1 - edge_length)
        # hold the random points
        dots.append(x)
        dots.append(y)
        dots.append(z)
        # ax.plot(x, y, z, label='curve')
        # draw the random points
        ax.scatter(x, y, z, c=colors[i], label=colors[i])

    # return all random points
    return dots


def generate_point(color='yellow'):
    """
    generate a single point and draw it.
    :param color: color of the point
    :return: location of a point
    """
    # get a random point
    x = np.random.random()
    y = np.random.random()
    z = np.random.random()
    # draw the point
    ax.scatter(x, y, z, c=color, label=color)
    # ax.text(x, y, z - 0.1, text, color=color)
    # return the point
    return x, y, z


# run
if __name__ == '__main__':
    # get figure object
    fig = plt.figure()
    # get 3d axis
    ax = fig.gca(projection='3d')

    # all points in a unit cube
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    ax.set_zlim3d(0, 1)
    # set labels for axises
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    print(generate_points(group_number=3, edge_length=0.2))
    print(generate_point())

    # show labels
    ax.legend()
    # show graph frame
    plt.show()
