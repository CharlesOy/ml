# -*- coding: utf-8 -*-
# 贝叶斯分类器


def bayes_classifier(data_set, categories, vec):
    """
    贝叶斯分类器
    :param data_set:先验数据
    :param categories:种类
    :param vec:目标向量
    :return:
    """
    result_p = 0
    result_c = None
    category_sum_count = 0
    for category in categories:
        category_sum_count += categories[category]
    for category in categories:
        cur_p = 1
        cur_p *= float(categories[category]) / category_sum_count
        for feature in vec:
            if data_set[feature] is None:
                continue
            cur_p *= float(data_set[feature][category]) / categories[category]
        if result_p < cur_p:
            result_p = cur_p
            result_c = category
    return result_c


if __name__ == '__main__':
    test_data = {}
    test_data.setdefault('data_set', {
        'python': {'bad': 0, 'good': 6},
        'the': {'bad': 2, 'good': 3},
        'money': {'bad': 3, 'good': 4}
    })
    test_data.setdefault('categories', {'bad': 5, 'good': 13})
    print(bayes_classifier(test_data['data_set'], test_data['categories'], ['the']))
