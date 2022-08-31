# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/22 16:38
from collections import deque

"""
    双端队列
    deque GIL 是线程安全的, list 不是线程安全的
"""

# user_list = ["H1", "H2"]
# user_name = user_list.pop()  # 取尾
# print(user_name, user_list)


# TODO .append() 将数据添加到 deque 的尾部
user_deque1 = deque(["H1", "H2", "H2"])  # def __init__(self, iterable=(), maxlen=None):
user_deque1.append("H3")
print(f"user_deque1: {user_deque1}")
#


print("---------------- 华丽的分割线 ----------------")
# TODO .appendleft() 将数据添加到 deque 的头部
user_deque2 = deque(["H1", "H2", "H2"])  # def __init__(self, iterable=(), maxlen=None):
user_deque2.appendleft("H0")
print(f"user_deque2: {user_deque2}")
#


print("---------------- 华丽的分割线 ----------------")
# TODO .clear() 清空队列中的所有数据
user_deque3 = deque(["H1", "H2", "H2"])  # def __init__(self, iterable=(), maxlen=None):
user_deque3.clear()
print(f"user_deque3: {user_deque3}")
#


print("---------------- 华丽的分割线 ----------------")
# TODO .copy() 对 deque 进行 浅拷贝
user_deque3 = deque(["H1", "H2", "H2"])  # def __init__(self, iterable=(), maxlen=None):
user_deque_copy = user_deque3.copy()
print("user_deque_copy:", user_deque_copy)
# 深拷贝, 直接用 Python 中深拷贝即可


print("---------------- 华丽的分割线 ----------------")
# TODO .count(value) 返回 value 出现的次数
user_deque4 = deque(["H1", "H2", "H2"])  # def __init__(self, iterable=(), maxlen=None):
print(user_deque4.count("H1"))
#


print("---------------- 华丽的分割线 ----------------")
# TODO .extend() 对 deque 元素进行扩展deque的右侧
user_deque5 = deque(["H1", "H2", "H2"])  # def __init__(self, iterable=(), maxlen=None):
ext_user_deque = deque(["H0", "H0"])
user_deque5.extend(ext_user_deque)
print(user_deque5)  # 是对自己进行扩容, 而不是返回一个新的 deque
#


print("---------------- 华丽的分割线 ----------------")
# TODO: .reverse() 对 deque 进行反转
user_deque6 = deque(["H1", "H2", "H2", "H3", "H4"])  # def __init__(self, iterable=(), maxlen=None):
user_deque6.reverse()
print("user_deque6", user_deque6)
#


print("---------------- 华丽的分割线 ----------------")
# TODO: .extendleft() 对 deque 元素进行扩展deque的左侧
#


print("---------------- 华丽的分割线 ----------------")
# TODO: .index() 查找元素
#


print("---------------- 华丽的分割线 ----------------")
# TODO: .insert() 指定位置插入 元素
#


