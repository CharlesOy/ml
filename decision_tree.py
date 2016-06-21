# -*- coding: utf-8 -*-
import math


def create_data_set():
    """
    create training data set
    :return:
    """
    return [[1, 1, 0], [1, 1, 0], [1, 0, 0], [0, 0, 1], [0, 0, 1]]


def calc_entropy(data_set):
    """
    calculate entropy for the data set
    :param data_set:
    :return: entropy
    """
    # calculate probability for each category
    total_count = len(data_set)
    entry_dict = {}
    for vec in data_set:
        if vec[-1] not in entry_dict:
            entry_dict.setdefault(vec[-1], 1)
        else:
            entry_dict[vec[-1]] += 1
    # calculate the entropy
    entropy = 0.0
    for entry in entry_dict:
        probability = float(entry_dict[entry]) / total_count
        entropy -= probability * math.log(probability, 2)
    return entropy


if __name__ == '__main__':
    print(calc_entropy(create_data_set()))
