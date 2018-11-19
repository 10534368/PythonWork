class User:
    def __init__(self):
        self.kahao="621700243002"
        self.key=""
        self.money=0
        self.ID=""
        self.idcard=""

    def show(self):
        print("卡号:%s持卡人:%s余额:%.2f"%(self.kahao,self.ID,self.money))

    def addmoney(self):
        Amoney=float(input("请输入存入金额:"))
        self.money+=Amoney
        print("存款成功,您的余额为:%.2f"%self.money)

    def popmoney(self):
        while True:
            Pmoney=float(input("请输入取出金额:"))
            if Pmoney>self.money:
                print("您的余额不足,请重新输入")
                continue
            self.money-=Pmoney
            print("取款成功,您的余额为:%.2f" % self.money)
            break

    def transfermoney(self,a):
        while True:
            transfermoney=float(input("请输入您要转出的金额:"))
            if transfermoney>self.money:
                print("您的余额不足,请重新输入")
                continue
            self.money-=transfermoney
            a.money+=transfermoney
            break
        print("转账成功!您的余额为%.2f"%self.money)

    def Ckey(self):
        while True:
            NEWkey=input("请设置您的新密码:")
            aNEWkey=input("请确认您的密码")
            if aNEWkey==NEWkey:
                self.key=NEWkey
                print("修改成功,请牢记您的新密码!")
                break
            else:
                print("两次输入的密码不一致!请重新输入!")