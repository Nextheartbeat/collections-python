# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/19 16:38
"""
    namedtuple 功能
        1.tuple 的 子类
        2.占用空间更小, 也没有创建类时的繁琐
        3.与 tuple 之间的转换
"""
from collections import namedtuple

User = namedtuple("User", ["name", "age", "height"])
user = User(name="Wjw", age=19, height=170)
print(user.name, user.age, user.height)
# 事实上, 我们 使用 MySQLclient 或 pymsql 读取数据时, 我们拿到的数据就是 tuple
print("----------华丽的分割线----------")
# TODO: 与 tuple 之间的转换
user_tuple = ("Wjw", 29, 175)
user_namedtuple = User(*user_tuple)
print(user_namedtuple.name, user_namedtuple.age, user_namedtuple.height)

print("----------华丽的分割线----------")


# TODO: 函数参数
def ask(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))


ask("wjw", 19, 170)
ask(name="wjw", age=19)  # 如果我们指定名称, 结果是这样的
print("----------华丽的分割线----------")
# 除了上面 *user_tuple 的传递方式之外, 我们还可以使用 dict 传递
user_dict = {
    "name": "Wjw",
    "age": 19,
    "height": 175
}
user_namedtuple_dict = User(**user_dict)
print(user_namedtuple_dict.name, user_namedtuple_dict.age, user_namedtuple_dict.height)