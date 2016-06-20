# -*- coding: utf-8 -*-
import math
import numpy as np


# K Nearest Neighbors algorithm
def cal_distance(vec1, vec2):
    """
    calculate the Euclidean distance of vec1 and vec2
    :param vec1:
    :param vec2:
    :return: distance
    """
    if len(vec1) != len(vec2):
        return -1
    return math.sqrt(sum(np.square(np.array(vec2) - np.array(vec1))))


def knn_classify(vec, data_set, labels, k):
    """
    K Nearest Neighbors algorithm
    :param vec: vector to be classified
    :param data_set: training data
    :param labels: labels of training data
    :param k: number of nearest neighbors to calculate
    :return: category of the vector
    """
    # store all the distances
    distances = []
    # store the sorted labels
    sorted_labels = []
    # iterate all vector in data_set
    for i, data in enumerate(data_set):
        # calculate the distance between current vector and vec
        cur_distance = cal_distance(vec, data)
        # insertion sort, insert current distance and label into the result lists(distance and sorted_labels)
        for j, stored_distance in enumerate(distances):
            if cur_distance < stored_distance:
                distances.insert(j, cur_distance)
                sorted_labels.insert(j, labels[i])
                break
        else:
            distances.append(cur_distance)
            sorted_labels.append(labels[i])
    # return the most common category in the list of top k sorted labels
    return most_common(sorted_labels[:k])


def most_common(lst):
    """
    get the most common element in a list
    http://stackoverflow.com/questions/1518522/python-most-common-element-in-a-list
    :param lst:
    :return:
    """
    return max(set(lst), key=lst.count)


if __name__ == '__main__':
    # test code
    _data_set = [[1, 1, 2], [2, 2, 1], [3, 4, 6], [2, 7, 3], [2, 3, 4]]
    _labels = [1, 1, 2, 2, 2]
    _vec = [3, 8, 1]
    print(knn_classify(_vec, _data_set, _labels, 3))
