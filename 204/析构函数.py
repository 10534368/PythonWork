#-*- coding: utf-8 -*-
# 在结束的时候自动执行的
# 执行时间:如果是全局,程序结束自动执行
# 局部函数执行完毕就自动执行

# class Person():
#     def __init__(self):
#         print("你出生了")
#     def __del__(self):
#         print("你走了")
# p=Person()
# del 删除 删除之后不能再次使用

# 垃圾回收(自动)

# 覆盖底层函数
# __str__()默认输出地址值
# print(p.__str__())

# __repr__()与__str__()相同

# 访问限制
# 私有,只能自己使用,别人不能使用

# 继承

# 有两只猫：一只叫小花，今年3岁白色。
# 另一只叫小白，今年3岁花色。
# class Cat:
#     def __init__(self):
#         self.__name=None
#         self.__age=None
#         self.__color=None
#     def setName(self,a):
#          self.__name=a
#     def setAge(self,b):
#          self.__age=b
#     def setColor(self,c):
#         self.__color=c
#     def getName(self):
#         return self.__name
#     def getAge(self):
#         return self.__age
#     def getColor(self):
#         return self.__color
#
# n=int(input("请输入猫的数量:"))
# b=[]
# list=[]
# for num in range(0,n):
#     b.append(num)
#     b[num]=Cat()
#     b[num].setName(input("名字"))
#     b[num].setAge(input("年龄"))
#     b[num].setColor(input("颜色"))
#     list.append(b[num].getName())
# while True:
#     name=input("请输入名字:")
#     a=0
#     for n in list:
#         if name==n:
#             print(b[list.index(n)].getName(),b[list.index(n)].getAge(),b[list.index(n)].getColor())
#             a=1
#             continue
#     if a==1:
#         break
#     print("没有这只猫，请重新输入")

# 继承
# 构造函数不能继承,会被覆盖

# class Animal:
#     def __init__(self):
#         self.name=None
#         print("父系")
# class Dog(Animal):
#     print("子系")
#     def __init__(self):
#         super().__init__()#超级调用
# d=Dog()
# print(d.name)
# a=Animal()
# print(a.name)

# 高内聚低耦合

# class Person:
#     def __init__(self):
#         self.name=None
#         self.age=None
#         self.sex=None
#         self.like=None
#         self.cn=None
#         self.WS= None
#     def show(self):
#         print("姓名:%s,年龄:%d,性别:%s,工龄或学号:%s\n我承诺,我会%s\n%s爱玩%s"%(self.name,self.age,self.sex,self.WS,self.cn,self.name,self.like))

# t=Person()
# t.name="王飞"
# t.age=30
# t.sex="男"
# t.cn="认真教课"
# t.like="象棋"
# t.WS="工龄为5"
# t.show()
#
# s=Person()
# s.name="小明"
# s.age=15
# s.sex="男"
# s.cn="好好学习"
# s.like="足球"
# s.WS="学号为00023102"
# s.show()

# class Animals:
#     def __init__(self,kind,shiwu):
#         self.kind=kind
#         self.name=None
#         self.shiwu=shiwu
#     def jinshi(self):
#         print("%s正在吃%s"%(self.kind,self.shiwu))
#
# class Person(Animals):
#     def __init__(self,kind,shiwu):
#         super().__init__(kind,shiwu)
#     def jinshi(self):
#         print("%s正在吃%s"%(self.name,self.shiwu))
#     def weishi(self,a):
#         print("%s喂过动物了"%self.name)
#         a.jinshi()
#
# p=Person("人","大米饭")
# p.name="小王"
# p.jinshi()
#
# d=Animals("狗","骨头")
# p.weishi(d)
#
# c=Animals("猫","鱼")
# p.weishi(c)

# 多态  一种事物的多种体现形式

# class Surface:
#     def __init__(self):
#         self.ver=[]
# for i in range(5):
#     s=Surface()
#     s.ver.append(i)
#     print(s.ver)