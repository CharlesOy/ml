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
    return [[1, 1, 0], [1, 1, 0], [1, 0, 0], [0, 0, 1], [0, 0, 1], [2, 2, 2], [2, 1, 1]], [0, 1]


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
    # calculate entropy for entry
    new_entropy = .0
    for value in value_dict:
        probability = float(value_dict[value]) / total_count
        new_entropy += probability * calc_entropy(split_data_set(data_set, entry, value))
    # return information gain
    return base_entropy - new_entropy


def calc_best_feature(data_set):
    """
    calculate the best feature of which information gain is the highest
    :param data_set:
    :return:
    """
    best_feature = 0
    best_ig = calc_information_gain(data_set, best_feature)
    for i in range(1, len(data_set[0]) - 1):
        cur_ig = calc_information_gain(data_set, i)
        if best_ig < cur_ig:
            best_ig = cur_ig
            best_feature = i
    return best_feature


def create_branch(data_set, labels):
    """
    create a decision tree branch
    :param data_set:
    :param labels:
    :return: a decision tree branch
    """
    categories = []
    for vec in data_set:
        categories.append(vec[-1])
    # if there is no feature in data set then return the most common category
    if len(data_set[0]) == 1:
        return max(set(categories), key=categories.count)
    # if there is only one category in data set then return it
    if len(categories) == categories.count(categories[0]):
        return categories[0]
    # calculate the best feature
    best_feature = calc_best_feature(data_set)

    branch = {labels[best_feature]: {}}
    # labels for next level, label of best feature removed
    labels_next_level = labels[:best_feature] + labels[best_feature + 1:]
    # storing handled values
    values = []
    # create children branches
    for vec in data_set:
        # if value not handled
        if vec[best_feature] not in values:
            values.append(vec[best_feature])
            # add branches to the tree
            branch[labels[best_feature]][vec[best_feature]] = create_branch(
                split_data_set(data_set, best_feature, vec[best_feature]), labels_next_level)
    # return the branch
    return branch


def classify(dt, labels, vec):
    """
    classify vector with decision tree
    :param dt: decision tree
    :param labels: feature labels
    :param vec: vector
    :return: category
    """
    key = dt.keys()[0]
    sub_tree = dt[key]
    key_index = labels.index(key)
    if type(sub_tree[vec[key_index]]).__name__ != 'dict':
        return sub_tree[vec[key_index]]
    else:
        return classify(sub_tree[vec[key_index]], labels, vec)


if __name__ == '__main__':
    # test code
    _data_set, _labels = create_data_set()
    _dt = create_branch(_data_set, _labels)
    _category = classify(_dt, _labels, [0, 0])
    print(_category)
