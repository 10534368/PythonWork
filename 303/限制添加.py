#-*- coding: utf-8 -*-
class Person:
    def __init__(self):
        pass
h=[0,1]
h[1]=Person()
# 限制添加属性
# __slots__=()除了括号内的其他变量禁止添加

# @property   #访问限制
