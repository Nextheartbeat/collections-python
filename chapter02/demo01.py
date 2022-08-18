# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/18 16:38
"""tuple的功能/不可变, iterable(可迭代的)"""
name_tuple = ("tuple1", "tuple2")
# 如果一个类实现了 __iter__, __getitem__ 这两个魔法方法, 那么这个类的对象就是一个可迭代的对象
for tp in name_tuple:
    print(tp)
# 如果我们对一个 tuple 进行修改的时候, 我们得到的是: 'tuple' object does not support item assignment 疑问: TODO python 变量是实质
# name_tuple[0] = "tuple3"

