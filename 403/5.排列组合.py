'''
排列组合：
    从n个元组中取出m个进行组合
    有顺序的，有重复的
'''
import itertools

list1=list(itertools.product("abcdAbcd01234.,-",repeat=8))
# print(list1)
mima="123456"

for i in list1:
    str1 = ""
    for j in i:
        str1+=str(j)
        # print(str1)
        if str1==mima:
            print("ok")
