# -*- coding: utf-8 -*-
def huanying():
    print("************欢迎进入手机淘宝************\n*****1,登陆*****\n*****2,退出*****")
    bian1 = str(input("请输入功能编号:"))
    if bian1 == "1":
        denglu()


def denglu():
    for i in range(1, 4):
        dic1 = {"张三": "zhangsan@qq.com", "李四": "zhangsanshishabi", "王麻子": "wocaishizhangsan",
                "小明": "xiaomingtianxiadiyi", "1": "1"}
        name = input("请输入用户名:")
        key = input("请输入密码:")
        m = dic1.get(name)
        if m != None and dic1[name] == key:
            print("登陆成功")
            zhuye()
        else:
            print("密码错误,您还有%d次机会" % (3 - i))
    print("您的机会已用完")


def zhuye():
    print("************欢迎进入手机淘宝************")
    list1 = ["今日特卖", "美食酷饮", "男女服饰", "电子产品", "儿童专区", "购物结算"]
    for i in range(len(list1)):
        print("*****%d," % (i + 1), list1[i], "*****")
    i = int(input("请输入功能编号:"))
    if i <= 5:
        qingdan(i)
    else:
        jiesuan()


def qingdan(i):
    list2 = [temaim, meishim, yifum, dianzim, ertongm]
    c = 1
    LIST = []
    for n, v in list2[i - 1].items():
        LIST.append(n)
        print("编号%d %s %0.2f元" % (c, n, v))
        c += 1
    bian = int(input("请输入要购买的商品编号:"))
    if gouwuche.get(LIST[bian - 1]) == None:
        gouwuche[LIST[bian - 1]] = list2[i - 1][LIST[bian - 1]]
    else:
        gouwuche[LIST[bian - 1]] += list2[i - 1][LIST[bian - 1]]
    zhiling = input("购买成功,是否继续:y/n\n")
    if zhiling == "y":
        qingdan(i)
    else:
        print("当前购物车商品列表如下:\n商品名称", "\t", "商品价格")
        for i, j in gouwuche.items():
            print(i, "\t", "%0.2f元" % j)
        zhuye()


def jiesuan():
    global gouwuche
    print("您本次购物商品列表如下:\n商品名称", "\t", "商品价格")
    sum = 0
    for i, j in gouwuche.items():
        print(i, "\t", "%0.2f元" % j)
        sum += j
    print("本次总共消费%0.2f元" % sum)
    zl = str(input("继续购物请按w,退出请按0\n"))
    if zl == "w":
        gouwuche = {}
        zhuye()
    elif zl == "0":
        print("谢谢您使用手机淘宝,下次再见!")
        exit()


import random

meishim = {"零食大礼包": 100, "**酸酸乳": 48, "**牛肉面": 30}
yifum = {"男士西装": 800, "女士连衣裙": 500, "皮鞋": 400, "高跟鞋": 400}
dianzim = {"笔记本电脑": 5000, "电冰箱": 3000, "空调": 3000}
ertongm = {"芭比娃娃": 100, "变形金刚": 200, "玩具大礼包": 500}
Mname = []
Yname = []
Dname = []
Ename = []
list3 = [Mname, Yname, Dname, Ename]
list4 = [meishim, yifum, dianzim, ertongm]
num = 0
for i in list3:
    for j in list4[num]:
        i.append(j)
    num += 1
temaim = {}
for num in range(len(list3)):
    STR = random.choice(list3[num])
    list4[num][STR] *= 0.8
    temaim[STR] = list4[num][STR]

gouwuche = {}
huanying()
print("谢谢您使用手机淘宝,下次再见!")
