# -*- coding: utf-8 -*-
# while n<=()
#
#     n=n+1
# while循环的结构
# while 适用于给出判断条件 循环过程中加入n=n+1以记录并达成不循环的条件  while可以实现无限循环
# for 适用于给出需要进行相同操作的数或者字符串 依次进行后续操作  for循环中 需要进行相同操作的对象数目是有限的
# break 中断循环 后续操作不执行结束循环
# contine 跳出单次循环 进行下一次循环

# print(abs())#求绝对值
# max(a,b,c)#求最大值
# min(a,b,c)#求最小值
# pow(a,b)求a的b次方
# round()四舍五入
# print(round(2.675,2))

# 在多个py文件中可能会出现相同的名字
# 为了不让名字之间冲突把不同的py文件放到不同的文件夹中import math
# print(math.ceil(3.1415926))向上取整
# print(math.floor(3.1415926))向下取整
# print(math.sqrt(3.1415926))#平方根
# print(math.modf(3.1415926))#返回小数和整数部分
# import random
# print(random.random)
# a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
# random.shuffle(a)
# print(a)
# import random
#
# print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
# print( random.random() )             # 产生 0 到 1 之间的随机浮点数
# print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
# print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
# print(random.sample([1,2,2,2],3))

# 创建字符串 字符串一旦创建不可更改
# 字符串可以做“+” “*”运算字符串只能和整数数字相乘
# a="0123456789"
# # print(a.index("j"))
# # print(a.rindex("j"))
# for num in range(len(a)):
#     if num<=100:
#         print(num,a[num])
# index 根据元素查找下标

# 截取切片
# print(a[0:5])
# print(a[5::2])
# print(len(a[5::2]))

# 替换 replace
# 大写 upper
# 小写 lower
# 大小写反转 swapcase
# 将每一个单词首字母大写并且其余字母小写 title
# 将整个字符串的首字母大写并且其余字母小写 capitalize

# 拆分 split("")
# 拼接 join
# a=['启明星的指引', '氤氲之息', '清泉流响']
# b="123456"
# print(b.join(a))
# 截取字符串最左边的符号   lstrip("符号")
# 截取字符串最右边的符号   rstrip("符号")
# 默认截取字符串最左边的符号   strip("符号")

# 指定字符串的长度为n 其余部分用"符号"填充 字符串左对齐 ljust(n,"符号")
# 指定字符串的长度为n 其余部分用"符号"填充 字符串右对齐 rjust
# 指定字符串的长度为n 其余部分用"符号"填充 字符串居中对齐 center
# 指定字符串的长度为n 其余部分用0填充 字符串右对齐 zfill

# 判断 startswich  endswich
# isalpha （字母） isalnum（字母或数字）  isupper（大写）  islower（小写） istitle（首字母大写） isdigit(数字)
# isspace（空格）

# 去掉引号 eval
# 格式化 format{} （占位符）

# a=b=c=1 abc同时赋值为一   a,b,c=1,2,3
# count()查找某一字符出现的次数

import time


def computer(a, fuhao, b):
    yunsuanfu = {"+": "sum", "-": "sub", "*": "ji", "/": "shang", "%": "quyu", "**": "mici", "//": "quzheng"}
    jieguo = ""
    for i, j in yunsuanfu.items():
        if fuhao == i:
            jieguo += str(a)
            jieguo += i
            jieguo += str(b)
            n = eval(jieguo)
            return ("两数%s:%d" % (j, n))
    return ("没有这个运算方式")


def ZhuangShi(f):
    def JiSuan(a, fuhao, b):
        n = time.clock()
        st = f(a, fuhao, b)
        l = len(st)
        print("*" * (l + 4))
        print(f(a, fuhao, b))
        print("*" * (l + 4))
        m = time.clock()
        print("程序执行时间:%f" % (m - n))

    return JiSuan


# 计算器(10,"*",2)

a = ZhuangShi(computer)
a(10, "-", 10)

# 输入输出
# 循环判断
#     判断 if    elif   else
#     循环 while for（初值 循环条件 递增递减条件）死循环 while True
# 变量
# 数据类型   type（）查看类型
#      整数 小数 字符串 布尔  空值
# 列表 元组 字典 集合
# 跟数字相关的函数
#     max（） min（）
#     abs（）取绝对值   round（）四舍五入
# math模块
#   ceil（）
# floor（）
# pow（）
# sqrt（）
# modf（）
# pi（）
# 字符串
#   字符串一旦创建不能修改  +（字符串） *（数字）  运算
#   查找
#   len（）
#   index   find     count（）
#   截取 拆分  替换 replace（旧的 新的 替换的个数）
#   大小写转换
#       upper（）
#       lower（）
#       反转swapcase（）
#       capitalize（）
#       title（）
#   判断：
#   拆分： 拆分结果为列表  spilt（）
#   拼接： 将列表的数据拼接为字符串 join（）
#   eval（）去引号
#   format（） 格式化
# 随机数rondom uniform randint randrange choice sample shuffle

#  len()获取列表的长度
# append()添加元素
# 删除元素
# remove   pop
# sort 升序排序
# reverse  倒序排序
# 浅复制 list1=list2
#
# 遍历
#
# 元组 创建后不可更改
# tup=()
# tup1=("a",)
# tup2=("A","b","c")
# tup3="a","s","a"
# print(type(tup))
# print(type(tup1))
# print(type(tup2))
# print(type(tup3))
# print(tup3)
# print(tup2)
# print(tup1)
# print(tup)
#
# 元组列表互相转换
# list=list(tup)
# tup=tuple(list)
# 字典
# for i in dict:#键
# for i,j in dict.items(): #键和值
# for i in dict.keys():  #键
# for i in dict.values():  #?值
# dict.clear()
# set
#     add   update
# pop  remove

# 1.去除列表中重复的元素
# m=int(input("请输入你要输入的列表中元素的个数："))
# list1=[]
# for num in range(1,m+1):
#     str=input("请输入第%d个字符串："%num)
#     list1.append(str)
# print(list1)
# list2=[]
# dict={}
# for j in list1:
#     dict[j]=j
# for i in dict:
#     list2.append(i)
# print(list2)
