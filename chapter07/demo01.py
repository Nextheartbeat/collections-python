# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/31 16:38
from collections import OrderedDict

"""
    OrderedDict: dict 的子类, 强化 dict
    有序字典
"""

user_dict = OrderedDict()
user_dict["a"] = "H1"
user_dict["b"] = "H2"
user_dict["c"] = "H3"
print(user_dict)

# .pop(key) # 传递一个值, 把他删除掉, 返回 value
_pop = user_dict.pop("a")
print(_pop)
print(user_dict)

# .popitem() # 删除最后一个, 返回键和值
user_dict["a"] = "H1"
print(user_dict)
_popitem = user_dict.popitem()
print(_popitem)
print(user_dict)

# .move_to_end(key) # 把某一个键, 放到最后
user_dict["a"] = "H1"
print(user_dict)
user_dict.move_to_end("b")
print(user_dict)
