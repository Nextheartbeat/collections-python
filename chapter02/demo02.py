# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo02.py
# time: 2022/8/18 16:38
"""tuple的功能/拆包||tuple不可变不是绝对的"""
"""拆包"""
user_tuple = ("Wjw", 21, 170)
name, age, height = user_tuple  # 分别映射, 位置对应关系
print(name, age, height)
# TODO: 什么? 你以为就这? 当然不是, 我们还可以
user_tuple_other = ("Wjw", 21, 170, "tianjin")
name, *other = user_tuple_other  # Wjw [21, 170, 'tianjin']
print(name, other)
print(type(name), type(other))
print("-------------->华丽的分割线<--------------")

"""tuple 不可变不是绝对的"""
tuple_demo = ("Wjw", [21, 170])
print(tuple_demo)
tuple_demo[1].append("tianjin")
print(tuple_demo)
# 这样确实发生了改变, 但是不推荐
# 不推荐把一个可变类型, 放到不可变类型中去

