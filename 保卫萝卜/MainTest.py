#-*- coding: utf-8 -*-
import time
from 保卫萝卜.炮塔 import Dpaota,Xpaota
from 保卫萝卜.怪物 import guaiwu
print("游戏开始!\n您可以建造萝卜炮和蘑菇炮来阻止怪物入侵!")
n=int(input("请输入建造萝卜炮的个数:"))
m=int(input("请输入建造蘑菇炮的个数:"))
list=[]
for i in range(1,n+m+1):
    if i<n+1:
        list.append("萝卜炮%d号"%i)
        list[i-1]=Xpaota(list[i-1])
    else:
        list.append("蘑菇炮%d号"%(i-n))
        list[i-1]=Dpaota(list[i-1])
num=1
while num<6:
    l=1000
    for i in range(3, 0, -1):
        print("\r倒计时{}秒...".format(i), end="")
        time.sleep(1)
    print("\r怪物入侵!当前第%d/5波"%num)
    g=guaiwu(num)
    while True:
        for i in range(len(list)):
            list[i].attack(g)
            if i < n:
                list[i].slowspeed(g)
            else:
                list[i].bingdong(g)
        if g.hp<=0:
            print("%s已被击杀!"%g.name)
            break
        time.sleep(1)
        l-=g.yisu
        print(l,g.hp)
        if l<=0:
            print("防守失败!")
            exit()
    num+=1
    if (num-1)%2==0:
        print("炮塔升级中!")
        time.sleep(3)
        for i in list:
            i.levelup()
print("胜利!")