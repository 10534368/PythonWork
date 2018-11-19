#-*- coding: utf-8 -*-
# 迭代器  一次取出一个值 只有是可迭代对象(能被for遍历的)才可以转换成迭代器  只有迭代器才可以做到一次取出一个值
# 生成器
from collections import Iterable
from collections import Iterator
import time
# print(isinstance([],Iterable))
# print(isinstance([],Iterator))
# print(isinstance(iter([]),Iterator))

# 转换成迭代器不会更改原可迭代对象  iter()
list1=[4,2,3,4,5,6]
l=iter(list1)
# print(next(list2))

# 生成器 yield语句就是一个生成器 生成器可以看做迭代器
def hanshu():
    for i in range(20, 81):
        if i % 3 == 0:
            yield i
a=hanshu()
# print(isinstance(a,Iterator))
# while True:
#     try:
#         print(next(a))
#     except StopIteration as e:
#         print("完了")
#         break

import random
list=[1,2,3,4,5,6,7,8,9,0]
# while True:
#     str1=""
#     n=random.randint(1, len(list))
#     for i in range(n):
#         str1+=str(random.choice(list))
#     if list1.count(str1)==0:
#         list1.append(str1)
#         # print(str1)
#         print("\r%d"%len(list1),end="")
#         # time.sleep(0.5)
#     else:
#         continue

# 排列 组合
str12="1238agimnox"
while True:
    str1=""
    n=random.randint(13,14)
    for i in range(n):
        str1+=str(random.choice(list))
    if list1.count(str1)==0:
        list1.append(str1)
        if str1=="xiaoming12138":
            print("ok")
            break
        print("\r%d"%len(list1),end="")
        # time.sleep(0.5)
    else:
        continue

