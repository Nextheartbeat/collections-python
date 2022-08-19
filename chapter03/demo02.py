# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo02.py
# time: 2022/8/19 16:38
"""
    _mask()
        : 可以让我们不用使用 **dict 的方式就能实现, namedtuple 对象的创建, 前提是字典中对营的名称, 数量要一致
源码
@classmethod
def _make(cls, iterable):
    result = tuple_new(cls, iterable)
    if _len(result) != num_fields:
        raise TypeError(f'Expected {num_fields} arguments, got {len(result)}')
    return result

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
