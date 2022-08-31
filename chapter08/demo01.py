# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/31 16:38
from collections import ChainMap

"""
    ChainMap
    可以将多个 dict, 进行统一处理
"""

user_dict1 = {"a": "H1", "v": "H2"}
user_dict2 = {"c": "H3", "d": "H4"}


new_dict = ChainMap(user_dict1, user_dict2)
new_dict = new_dict.new_child({"b": "H5"})  # 添加一个 dict 返回一个新的 ChainMap 对象
print(new_dict)
print(new_dict["c"])
# 进行迭代
for key, value in new_dict.items():
    print(key, value)

# 如果, key 重复, 之后打印首次出现的 key
new_dict = new_dict.new_child({"b": "H7"})
print(new_dict)
for key, value in new_dict.items():
    print(key, value)

# TODO: 重点 maps 它是一个实例而不是 copy

print(new_dict.maps)
new_dict.maps[0]["b"] = "H9"
print(new_dict)