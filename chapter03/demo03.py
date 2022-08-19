# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo02.py
# time: 2022/8/19 16:38
"""
    _asdict()
    : 可以将 namedtuple 对象, 转换为 dict
"""
from collections import namedtuple

user_dict_data = {
    "name": "Wjw",
    "age": 19,
    "height": 170
}
User = namedtuple("User", ["name", "age", "height"])
user_dict = User._make(user_dict_data)
print(user_dict.name, user_dict.age, user_dict.height)
"""namedtuple 支持拆包"""
name, *other = user_dict
print(name, other)
"""Demo"""
user_info_dict = user_dict._asdict()
print(user_info_dict)
print(isinstance(user_info_dict, dict))
print(type(user_info_dict))
