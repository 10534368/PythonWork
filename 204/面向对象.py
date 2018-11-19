#-*- coding: utf-8 -*-
# 面向对象 注重设计  从设计角度设计代码,追求的是代码的维护性和拓展性
# 封装 继承 多态
# 面向过程 注重结果  以结果出发考虑问题

# 设计植物大战僵尸程序
# 植物的类型 僵尸的类型
# 不同类型不同属性不同作用

# 比函数稍微大一点的容器叫做类
# 可以放很多函数和变量
# 把同一类事物的代码放到类中去
# class
# class SunFlower:
#     hp=100
#     def yao(self):
#         pass
#     def die(self):
#         pass
# class wandou:
#     hp=100

# 类是一个图纸
# 对象是根据图纸创建具体物体

# 设计一个人类,年龄 身高 姓名 体重 吃饭 睡觉 性别
# class Paple:
#     name="NPC"
#     age=0
#     height=None
#     weight=None
#     def eat(self):
#         print("%s吃饭"%self.name)
#     def sleep(self):
#         print("%s睡觉"%self.name)
#
# p1=Paple()
# p1.name="小明"
# p1.age=20
# p1.weight=100
# p1.height=160
# p1.eat()
# p1.sleep()

# 封装
# 类 函数 模块
# 先分析有哪些事物
# 这类事物的信息就是属性 做什么事情就是作用
# 类是由属性跟作用构成的
# 属性=变量 行为=函数

# 构造函数
# 当类当中没有变量的时候,通过对象名,变量是可以自动的创建出变量,但这个变量只能自己使用
# 创建变量 初始化赋值

# class Person:
    # 写构造函数
    # self.变量名   创建变量
    # self  自己(谁调用self就代表谁)_
#     def __init__(self):
#         self.name=""
#         self.age=0
#         self.sex=None
#         print("你出生了")
# p1=Person()
# p1.__init__()
# 实例化
# 创建对象默认调用构造函数

# class 小兵:
#     def __init__(self):
#         pugong=10
#         hp=400
#         hujia=29
#         mokang=33
#         print("击杀可获得14金币")
# p1=小兵()

# 2只手交换牌
# class Huanpai:
#     def __init__(self):
#         self.zs="大王"
#         self.ys="小王"
#
# p1=Huanpai()
# p1.zhuozi=p1.zs
# p1.zs=p1.ys
# p1.ys=p1.zhuozi
# print(p1.zs)
# print(p1.ys)

# ren shou pai

# import random,time
# color=[1,2,3,4,5,6]
# sum=0
# num=0
# while True:
#     n=random.choice(color)
#     sum+=n
#     num+=1
#     print(n)
    # time.sleep()
# print(num)

# 枪：qiang
# 属性：子弹数量
# 行为：发射子弹
# 人：Person
# 属性:枪,眼睛
# 行为：开枪

# class Person():
#     def __init__(self):
#         self.hand=""
#         self.eye=""
#     def kaiqiang(self):
#         self.banji=self.hand
#         if self.banji=="1":
#             print("biu")
#         self.banji="0"
#
# class Qiang():
#     def __init__(self):
#         self.banji=""
#         self.zidanshuliang=0
# class Hand():
#     def __init__(self):
#         self.right_hand=""
#         self.left_hand=""

# class Person:
#     def __init__(self,a,b):
#         self.name=a
#         self.age=b
#         print("姓名:%s"%self.name,"年龄:%d"%self.age)
#
# p1=Person
# p2=p1("小明",21)
# p2.name="UZI"
# p2.age=21
