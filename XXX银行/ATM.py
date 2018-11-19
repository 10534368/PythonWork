import pickle
import random
import time

from XXX银行.USER import User


class Atm:
    def __init__(self):
        self.Gname = "小明"
        self.Gkey = "12138"
        self.menu = {"1": "开户", "2": "查询", "3": "存款", "4": "取款", "5": "转账", "6": "改密", "7": "锁定", "8": "解锁", "9": "销户",
                     "t": "退出"}
        self.Udic = {}
        self.lockdic = {}
        try:
            path = r"D:\PythonWork\XXX银行\cun"
            f = open(path, "rb")
            self.Udic = pickle.load(f)
            self.lockdic = pickle.load(f)
        except EOFError as e:
            print(e)
        self.login()

    def login(self):
        print("----------------欢迎来到XXX银行----------------")
        gname = input("请输入管理员账号:")
        gkey = input("请输入管理员密码:")
        if gname == self.Gname and gkey == self.Gkey:
            print("登陆成功,正在为您加载页面,请稍后...")
            time.sleep(2)
            self.homepage()
        else:
            print("验证未成功,登陆失败!")
            exit()

    def homepage(self):
        print("*" * 21)
        n = 1
        for i, j in self.menu.items():
            if n % 2 == 0:
                print("%s(%s)" % (j, i), "*")
            elif n % 2 != 0:
                print("*", "%s(%s)" % (j, i), end="\t")
            n += 1
        print("*" * 21)
        while True:
            print(self.Udic, self.lockdic)
            zl = input("请输入要执行的操作:")
            if zl == "1":
                self.origin()
            elif zl == "2" or zl == "3" or zl == "4":
                self.qianrenzheng(zl)
            elif zl == "5":
                self.Transferaccounts()
            elif zl == "6":
                self.ChangePassword()
            elif zl == "7":
                self.locking(input("请输入卡号:"), input("请输入密码:"))
            elif zl == "8":
                self.Unlock()
            elif zl == "9":
                self.Sales()
            elif zl == "t":
                path = r"D:\PythonWork\XXX银行\cun"
                f = open(path, "wb")
                pickle.dump(self.Udic, f)
                pickle.dump(self.lockdic, f)
                f.close()
                print("请妥善保管您的私人物品!")
                exit()
            else:
                print("指令输入错误,请重新输入!")

    # zl=1
    def origin(self):
        while True:
            user = input("请输入您的用户名:")
            idcard = input("请输入您的身份证号:")
            key = input("请设置您的密码:")
            Akey = input("请确认您的密码:")
            money = int(input("请输入您的预存金额:(不得低于10块)"))
            if key != Akey:
                print("两次输入的密码不一致!请重新输入!")
                continue
            elif money < 10:
                print("预存金额不得低于10块!请重新输入!")
                continue
            else:
                break
        while True:
            u = User()
            for i in range(0, 7):
                u.kahao += random.choice("1234567890")
            if self.Udic.get(u.kahao) is None:
                print("开户成功,您的卡号为:", u.kahao)
                break
        u.key = key
        u.money = float(money)
        u.ID = user
        u.idcard = idcard
        self.Udic[u.kahao] = u
        self.homepage()

    def Transferaccounts(self):
        num = 3
        enterID = input("请输入您要转入金额的卡号:")
        outID = input("请输入您要转出金额的卡号:")
        while num > 0:
            KEY = input("请输入密码:")
            if self.lockdic.get(outID) != None:
                print("您的卡已被锁定,请前往解锁")
                break
            elif self.lockdic.get(enterID) != None:
                print("您要转入的卡已被锁定")
                break
            elif self.Udic.get(outID) == None:
                print("卡号不存在,请先开户")
                break
            elif KEY == self.Udic[outID].key:
                self.Udic[outID].transfermoney(self.Udic[enterID])
                self.homepage()
            else:
                num -= 1
                print("密码错误,请重新输入,您还有%d次机会" % num)
        else:
            print("您的次数已用完!")
            self.locking(outID, self.Udic[outID].key)

    def ChangePassword(self):
        num = 3
        ID = input("请输入卡号:")
        while num > 0:
            IDCARD = input("请输入身份证号:")
            KEY = input("请输入密码:")
            if self.lockdic.get(ID) != None:
                print("您的卡已被锁定,请前往解锁")
                break
            elif self.Udic.get(ID) == None:
                print("卡号不存在,请先开户")
                break
            elif KEY == self.Udic[ID].key and IDCARD == self.Udic[ID].idcard:
                self.Udic[ID].Ckey()
                self.homepage()
            else:
                num -= 1
                print("密码错误,请重新输入,您还有%d次机会" % num)
        else:
            print("您的次数已用完!")
            self.locking(ID, self.Udic[ID].key)

    def locking(self, a, b):
        self.KEY = b
        if self.KEY == self.Udic[a].key:
            self.lockdic[a] = self.Udic[a]
            del self.Udic[a]
            print("您的账户已被锁定,请前往解锁")
        else:
            print("密码错误")
        self.homepage()

    def Unlock(self):
        ID = input("请输入卡号:")
        IDCARD = input("请输入身份证号:")
        KEY = input("请输入密码:")
        if self.Udic.get(ID) != None:
            print("您的卡正常,不需要解锁")
        elif self.Udic.get(ID) == None and self.lockdic.get(ID) == None:
            print("卡号不存在,请先开户")
        elif KEY == self.lockdic[ID].key and IDCARD == self.lockdic[ID].idcard:
            self.Udic[ID] = self.lockdic[ID]
            del self.lockdic[ID]
            print("解锁成功,您的卡可以正常使用了!")
        else:
            print("验证失败,如果忘记密码,请您持有效证件前往营业厅人工服务处解除锁定并更改密码!")
        self.homepage()

    def Sales(self):
        num = 3
        ID = input("请输入卡号:")
        while num > 0:
            IDCARD = input("请输入身份证号:")
            KEY = input("请输入密码:")
            if self.lockdic.get(ID) != None:
                print("您的卡已被锁定,请前往解锁")
                self.homepage()
            elif self.Udic.get(ID) == None:
                print("此卡号不存在!")
                self.homepage()
            elif KEY == self.Udic[ID].key and IDCARD == self.Udic[ID].idcard:
                del self.Udic[ID]
                print("您的账户已注销!")
                self.homepage()
            else:
                num -= 1
                print("密码错误,请重新输入,您还有%d次机会")
        else:
            print("您的次数已用完!")
            self.locking(ID, self.Udic[ID].key)

    def qianrenzheng(self, a):
        ID = input("请输入卡号:")
        for i in range(0, 3):
            KEY = input("请输入密码:")
            if self.lockdic.get(ID) != None:
                print("您的卡已被锁定,请前往解锁")
                break
            elif self.Udic.get(ID) == None:
                print("卡号不存在,请先开户")
                break
            elif KEY != self.Udic[ID].key:
                print("密码错误,请重新输入,您还有%d次机会" % (2 - i))
            else:
                if a == "2":
                    self.Udic[ID].show()
                elif a == "3":
                    self.Udic[ID].addmoney()
                elif a == "4":
                    self.Udic[ID].popmoney()
                self.homepage()
        else:
            print("您的次数已用完!")
            self.locking(ID, self.Udic[ID].key)
