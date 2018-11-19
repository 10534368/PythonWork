#-*- coding: utf-8 -*-
# sorted 排序  不会更改原列表
# sort 会更改原列表
list1=[1,2,35,6,8,4,9,4,6,-123,0]
list2=sorted(list1,key=abs)
print(list1)
print(list2)
list1.sort(reverse=True)
print(list1)
# reverse=True降序  False升序
list4=["hgvuyfu","fjoiah","57643148"]
list3=sorted(list4,key=len)
print(list3)

# @staticmethod   #静态函数
def hanshu():
    pass

'''
序列化和反序列化
pickle   json
序列化 存  反序列化  取
文件操作 1 打开文件 open
        2 读写操作
        3 关闭文件
'''
import pickle
# a=pickle.dumps(list1)#将list1中的数据序列化到a中   二进制
# print(a)
# b=pickle.loads(a)
# print(b)

# pickle.dump()序列化并存储到文件中
# pickle.load()将文件中的数据反序列化读取出来