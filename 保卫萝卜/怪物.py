#-*- coding: utf-8 -*-
class guaiwu:
    def __init__(self,a):
        self.name="怪物%d号"%a
        self.hp=200*a
        self.yisu=100+10*a
        print("%s来袭,血量为%d,移速为%d/s"%(self.name,self.hp,self.yisu))