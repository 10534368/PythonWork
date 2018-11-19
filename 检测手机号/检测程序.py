# -*- coding: utf-8 -*-
import re


class Check:
    def __init__(self):
        self.name = "手机号检测小程序"
        print("欢迎使用%s" % self.name)

    def Echeck(self, a):
        if re.findall("[^0-9]", a) == [] and len(a) == 11 and re.match("1", a) != None:
            self.check(a)
        else:
            print("不是手机号!")

    def check(self, a):
        if re.findall("(13[4-9]|147|15[0-2]|15[7-9]|178|18[2-4]|18[7-8]|198)", a[0:3]) != []:
            print("中国移动")
        elif re.findall("(13[0-2]|15[5-6]|145|176|18[5-6]|166)", a[0:3]) != []:
            print("中国联通")
        elif re.findall("(1[3|5]3|149|17[3|7]|18[0-1]|1[8|9]9)", a[0:3]) != []:
            print("中国电信")
        else:
            print("目前还不是手机号")

    def __del__(self):
        print("谢谢使用")


c = Check()
while True:
    c.Echeck(input("请输入一个手机号:"))
    zl = input("请选择继续检测还是退出(任意键继续n退出)")
    if zl == "n":
        exit()
