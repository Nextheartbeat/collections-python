# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/19 16:38
from collections import defaultdict

"""defaultdict 功能"""
"""实现统计"""
# user_dict = {}
# users = ["Heartbeat1", "Heartbeat1", "Heartbeat2", "Heartbeat3",
#          "Heartbeat1", "Heartbeat2", "Heartbeat3"]
# for user in users:
#     if user not in user_dict:
#         user_dict[user] = 1
#     else:
#         user_dict[user] += 1
# print(user_dict)

"""dict 内置方法 setdefault()
    如果 传递的第一个参数不存在 就添加到 dict 中 默认值为第二个参数
    性能更加高效, 会少做一次查询操作
"""
# user_dict = {}
# users = ["Heartbeat1", "Heartbeat1", "Heartbeat2", "Heartbeat3",
#          "Heartbeat1", "Heartbeat2", "Heartbeat3"]
# for user in users:
#     user_dict.setdefault(user, 0)
#     user_dict[user] += 1
# print(user_dict)

"""defaultdict
    当调用的键不存在的时候, 会自动添加键, 值为传递的可调用对象的默认值
    应用场景, 数据处理, 初始化
"""
# default_dict = defaultdict(int)  # 可调用的对象
# print(default_dict["Heartbeat"])  # defaultdict(<class 'list'>, {'Heartbeat': []})
# print(default_dict)
# pass
# users = ["Heartbeat1", "Heartbeat1", "Heartbeat2", "Heartbeat3",
#          "Heartbeat1", "Heartbeat2", "Heartbeat3"]
# for user in users:
#     default_dict["user"] += 1

"""
    实现 嵌套 dict,
    传递的值, 必须是一个可调用对象, 函数也是一个可调用对象
"""


def gen_default():
    return {
        "name": "",
        "age": 0
    }


default_dict = defaultdict(gen_default)
print(default_dict["Heartbeat"])
print(default_dict)
