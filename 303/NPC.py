#-*- coding: utf-8 -*-
class NPC:
    def __init__(self,a,b,c,d):
        self.name=a
        self.explain=b
        self.number=c
        self.NPC_list=d
    def show(self):
        print(self.number,self.name,self.explain)

class Player:
    def __init__(self):
        self.team_list=[]
    def addNPC(self,n):
        self.team_list.append(n)
    def delNPC(self,num):
        del self.team_list[num]

import random
dic={"阿尔萨斯":"使用霜之哀伤的怒火攻击敌人","吉安娜":"使用奥术法术远程打击敌人","乌瑟尔":"使用圣光的力量治愈盟友","小明":"什么也不会"}
Nlist=[]
for i in dic:
    Nlist.append(i)
n=random.randint(2,len(Nlist))
N=[]
for num in range(0,n):
    name=random.choice(Nlist)
    Nlist.remove(name)
    N.append(name)
    N[num]=NPC(name,dic[name],num+1,N)
p=Player()
while True:
    print("可选NPC")
    for num in range(0, n):
        N[num].show()
    print("当前队伍NPC")
    for num in range(len(p.team_list)):
        p.team_list[num].show()
    cz=input("请选择您要进行的操作\n1,邀请组队\n2,踢出队伍\n0,完成\n")
    if cz=="1":
        id=int(input("请选择可选NPC列表中要邀请组队的NPC的ID:\n"))
        if id-1>=len(N):
            print("编号错误,没有这个编号")
            continue
        if p.team_list.count(N[id-1])>0:
            print("要邀请的NPC已在队伍中")
            continue
        p.addNPC(N[id-1])
    elif cz=="2":
        id=int(input("请选择当前队伍NPC列表中要踢出队伍的NPC的ID:\n"))
        if p.team_list.count(N[id-1])==0:
            print("编号错误,你选择的ID不在队伍中")
            continue
        p.delNPC(p.team_list.index(N[id-1]))
    elif cz=="0":
        break
    else:
        print("操作指令错误,请重新选择")
