# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo03.py
# time: 2022/8/19 16:38
"""
    tuple 比 list 好的地方
    1. immutable的重要性:
        1). 性能优化: 指出元素全部为 immutable 的 tuple 会作为常量在编译时确定, 因此产生显著的速度差异
        1). 线程安全
        3). 可以作为 dict 的 key: 可哈希的
        4). 拆包特性
    如果拿C语言来类比, Tuple 对应的是 struct 而 list 对应的是 array

"""
user_tuple = (1, 2)
user_list = [1, 2]
user_info_dict = {}
user_info_dict[user_tuple] = 1
print(user_info_dict)  # {(1, 2): 1}

user_info_dict[user_list] = 2  # TypeError: unhashable type: 'list'
