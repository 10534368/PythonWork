#-*- coding: utf-8 -*-
# 有一对兔子，从出生后第3个月起每个月都生一对兔子，，假如兔子都不死，问每个月的兔子总数为多少？
class Rabbits:
    def __init__(self):
        self.double=[0,1]
    def shengyu(self,n):
        if n>=2:
            self.double.append(self.double[n-2]+self.double[n-1])
        print("第%d个月有%d对兔子"%(n,self.double[n]))

r=Rabbits()
mon=1
while mon<=20:
    r.shengyu(mon)
    mon+=1
# while mon>0:
#     r.shengyu(num)
#     num+=1

# 模拟ATM机存取款操作
class ATM:
    def __init__(self):
        print("欢迎使用ATM机！\n请插入您的银行卡")
        self.money=1000
        self.Key="443368"
        self.yanzheng()
    def __del__(self):
        print("请收好您的磁卡,欢迎下次光临！")
    def yanzheng(self):
        cs=3
        while cs>0:
            key=input("请输入银行卡密码：")
            if key==self.Key:
                print("读卡成功！")
                self.cunqukuan()
                cs-=3
            else:
                cs-=1
                print("密码错误，您还有{}次机会！".format(cs))
                if cs==0:
                    print("您的次数已用完！")
    def cunqukuan(self):
        while True:
            operation=int(input("请选择您要进行的操作：1.查询，2.存款，3.取款，4.退卡"))
            if operation==1:
                print("当前卡内余额：{}".format(self.money))
                continue
            elif operation==2:
                save=int(input("请输入存款金额："))
                self.money+=save
                print("存款成功，当前余额为：{}".format(self.money))
                continue
            elif operation==3:
                quchu=int(input("请输入取款金额："))
                if quchu > self.money:
                    print("余额不足，请重新输入！")
                    continue
                self.money-=quchu
                print("取款成功，当前余额为：{}".format(self.money))
                continue
            elif operation==4:
                break
            else:
                print("操作指令错误，请重新输入！")
                continue