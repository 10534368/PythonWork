#-*- coding: utf-8 -*-
# 用户在注册账号的时候我们需要输入用户信息，创建一个用户类，变量有：用户名、密码、性别。要求：用户名必须以字母开头，密码必须是6位以上，性别只能是男和女。写一个show方法打印用户名、密码、性别的信息。在主函数中创建一个用户对象，给三个变量赋值，如果赋值不满足要求则重新输入。否则调用show方法输出信息即可
class User:
    def __init__(self):
        self.name=None
        self.key=None
        self.sex=None
    def show(self):
        print("用户名:%s,密码:%s,性别:%s"%(self.name,self.key,self.sex))

u=User()
while True:
    name=input("请输入用户名(名字必须以字母开头):")
    if name[0].isalpha()==True:
        u.name=name
        break
    else:
        print("名字必须以字母开头,请重新输入")
while True:
    key=input("请输入密码(密码必须6位以上):")
    if len(key)>=6:
        u.key=key
        break
    else:
        print("密码必须6位以上,请重新输入")
while True:
    sex=input("请输入性别(男或女):")
    if sex=="男" or sex=="女":
        u.sex=sex
        break
    else:
        print("请输入男或女")
u.show()
