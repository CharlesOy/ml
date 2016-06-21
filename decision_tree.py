# -*- coding: utf-8 -*-
"""
Decision Tree
by Charles Ouyang
2016.06.21
"""
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
    entropy = .0
    for entry in entry_dict:
        probability = float(entry_dict[entry]) / total_count
        entropy -= probability * math.log(probability, 2)
    return entropy


def split_data_set(data_set, entry, value):
    """
    get child data set while value of specific entry of origin data set is specific
    :param data_set:
    :param entry:
    :param value:
    :return: split data set
    """
    data_result = []
    for vec in data_set:
        if vec[entry] == value:
            data_result.append(vec[:entry] + vec[entry + 1:])
    return data_result


def calc_information_gain(data_set, entry):
    """
    calculate information gain for data set and specific entry
    :param data_set:
    :param entry:
    :return: information gain
    """
    total_count = len(data_set)
    base_entropy = calc_entropy(data_set)
    value_dict = {}
    for vec in data_set:
        if vec[entry] not in value_dict:
            value_dict.setdefault(vec[entry], 1)
        else:
            value_dict[vec[entry]] += 1
    new_entropy = .0
    for value in value_dict:
        probability = float(value_dict[value]) / total_count
        new_entropy += probability * calc_entropy(split_data_set(data_set, entry, value))
    # return information gain
    return base_entropy - new_entropy


if __name__ == '__main__':
    print(1, calc_entropy(create_data_set()))
    print(2, calc_information_gain(create_data_set(), 0))
    print(3, calc_information_gain(create_data_set(), 1))
