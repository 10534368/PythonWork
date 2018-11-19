#-*- coding: utf-8 -*-
import time
class Paota:
    def __init__(self,name):
        self.name=name
        self.gjl=None
    def attack(self,b):
        print("看到我你就输了")
    def levelup(self):
        self.gjl*=2
        print("%s升级成功,攻击力*2,当前攻击力为%d"%(self.name,self.gjl))

class Xpaota(Paota):
    def __init__(self,name):
        super().__init__(name)
        self.gjl=20
        print("%s建造完成,攻击力为%d,能对单目标进行攻击!"%(self.name,self.gjl))
    def attack(self,b):
        b.hp-=self.gjl
        print("%s进行单体输出.........."%self.name)
    def slowspeed(self,b):
        n=b.yisu
        b.yisu/=2
        time.sleep(1)
        b.yisu=n
        print("%s释放技能减速"%self.name)

class Dpaota(Paota):
    def __init__(self,name):
        super().__init__(name)
        self.gjl=10
        print("%s建造完成,攻击力为%d,能对群体目标进行攻击!"%(self.name,self.gjl))
    def attack(self,b):
        b.hp-=self.gjl
        print("%s进行群体输出::::::::::"%self.name)

    def bingdong(self,b):
        n = b.yisu
        b.yisu = 0
        time.sleep(0.5)
        b.yisu = n
        print("%s释放技能冰冻" % self.name)