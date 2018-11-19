#-*- coding: utf-8 -*-
# 定义一个英雄类，包含玩家数量，生命值，攻击力和玩家姓名，同时包含一个方法攻击方法，调用攻击方法时显示如图信息，构造函数中需要初始化数据，当玩家加入游戏后需要显示玩家姓名和数量
import random
class Hero:
    def __init__(self,a):
        self.name=a
        self.hp=random.randint(100,150)
        self.ad=self.hp//10
        d=len(h)
        print("新玩家%s加入游戏,当前游戏玩家数量为%d"%(self.name,d))
    def gongji(self):
        num=0
        while num<len(h):
            if num==len(h)-1:
                if h[0].hp<=h[num].ad:
                    h[0].hp=0
                else:
                    h[0].hp-=h[num].ad
                print("玩家%s对玩家%s进行攻击,造成%d伤害,玩家%s剩余hp为%d"%(h[num].name,h[0].name,h[num].ad,h[0].name,h[0].hp))
                if h[0].hp==0:
                    print("玩家%s被击杀,淘汰出局" % h[0].name)
                    h.pop(0)
            else:
                if h[num+1].hp<=h[num].ad:
                    h[num+1].hp=0
                else:
                    h[num+1].hp-=h[num].ad
                print("玩家%s对玩家%s进行攻击,造成%d伤害,玩家%s剩余hp为%d" %(h[num].name, h[num+1].name, h[num].ad, h[num+1].name, h[num+1].hp))
                if h[num+1].hp==0:
                    if num+1==len(h)-1:
                        print("玩家%s被击杀,淘汰出局" % h[num+1].name)
                        h.pop(num+1)
                        break
                    print("玩家%s被击杀,淘汰出局" % h[num+1].name)
                    h.pop(num+1)
            num+=1

n=int(input("请输入玩家的数量:"))
h=[]
for num in range(0,n):
    h.append(num)
    h[num]=Hero("机器人%d号"%(num+1))
while n>1:
    while len(h)>1:
        h[0].gongji()
        zl=input("请按任意键继续")
    print("玩家%s获胜" % h[0].name)
    break
