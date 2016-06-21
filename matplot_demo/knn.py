# -*- coding: utf-8 -*-
"""
this Python script is for displaying k nearest neighbors algorithm
"""
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


class Knn:
    """
    knn class
    """

    def __init__(self):
        pass

    @staticmethod
    def generate_points(group_number=2, edge_length=0.2, point_number=10):
        """
        generating some groups of points
        :param group_number: number of groups
        :param edge_length: every group of points will distributes in a small cube,
        edge_length is the edge length of the cube
        :param point_number: number of points
        :return: the random points
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

        dots = []
        for i in range(group_number):
            # get random points
            x = np.random.sample(point_number) * edge_length + np.random.random() * (1 - edge_length)
            y = np.random.sample(point_number) * edge_length + np.random.random() * (1 - edge_length)
            # hold the random points
            dots.append([(x[j], y[j]) for j in range(len(y))])
            # ax.plot(x, y, z, label='curve')

        # return all random points
        return dots

    @staticmethod
    def generate_point():
        """
        generate a single point
        :return: location of a point
        """
        # get a random point
        x = np.random.random()
        y = np.random.random()
        # return the point
        return x, y

    @staticmethod
    def demo_points():
        """
        :return: some demo clustered points and a specific unclustered point
        """
        return [[[(0.48811123155852182, 0.40427992236129606), (0.36436741045897797, 0.3201858889243559),
                  (0.45936035486498655, 0.22824658846519891), (0.41060920703987663, 0.4328192536022577),
                  (0.4984746275268539, 0.34187623147576229), (0.7062156156205539, 0.46803497234111258),
                  (0.65475036303718526, 0.22297458995774205), (0.42788733293114445, 0.44749974412552579),
                  (0.68975728131047909, 0.30552167368852673), (0.55579463513384486, 0.21841173531043345)],
                 [(0.29470352641833175, 0.58484290623682456), (0.21561569171033851, 0.3929262312749906),
                  (0.2945759190496009, 0.4444944646985256), (0.26173575698477508, 0.46129046979728849),
                  (0.18992478407033381, 0.47234255443093609), (0.43922960238737802, 0.57094231848413624),
                  (0.1244511079911973, 0.53751194546220404), (0.16087158157153081, 0.77129947530020271),
                  (0.50511948184411659, 0.48326818288692019), (0.2973150099597916, 0.4778766129813351)],
                 [(0.87503155769989194, 0.45517727609523101), (0.41334730620637294, 0.5031505655919315),
                  (0.63662500509599218, 0.27456158167595268), (0.72333174390989896, 0.56219575139868694),
                  (0.75455626737887327, 0.57602624016841864), (0.71034176005955774, 0.53476519422517832),
                  (0.44245741424776214, 0.26176604783944873), (0.90693323721537378, 0.23291896498554893),
                  (0.54903063890613124, 0.45821227851735352), (0.7336812236770538, 0.56172698418801636)]], (
                    0.3966300707600645, 0.36133536671717115)]


def draw_points(points, color, label=None):
    """
    draw points
    :param points: specific points
    :param color: color of the points
    :param label: label of the points
    :return:
    """
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    if label is None:
        label = color
    ax.scatter(x, y, c=color, label=label)


# run
if __name__ == '__main__':

    knn = Knn()

    # get figure object
    fig = plt.figure()
    # get 3d axis
    ax = fig.gca()

    # all points in a unit cube
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    # set labels for axises
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')

    colors = ['red', 'green', 'blue']
    for _i, _points in enumerate(knn.demo_points()[0]):
        draw_points(_points, colors[_i])
    draw_points([knn.demo_points()[1]], 'yellow')

    # show labels
    ax.legend()
    # show graph frame
    plt.show()
