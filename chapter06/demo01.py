# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/31 16:38
from collections import Counter

"""
    Counter: dict 的子类
"""

users = ["H1", "H2", "H3", "H1", "H2", "H3", "H1", "H2", "H3"]
counter_user = Counter(users)  # self, iterable=None, /, **kwds
print(counter_user)  # 实现数量统计, 可迭代对象, 进行统计
counter_user.update(["H1"])  # 添加一个,
print(counter_user)
# 还可以处理 Top N 的问题, 比如取数量最多的前两个
print(counter_user.most_common(2))  # _heapq: 也是数据结构, 堆
