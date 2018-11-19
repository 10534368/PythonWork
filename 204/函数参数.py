#-*- coding: utf-8 -*-
# def fun(*args,**kwargs):

# args 元组  kwargs 字典

# os模块
# import os
# print(os.name)   #查看操作系统的类型

# print(os.uname())    #打印系统的详细信息 Windows不支持
# print(os.environ)
# print(os.environ.get("PATH"))
# print(os.getcwd())  #CURRENT当前文件所在的路径
# print(os.listdir())   # 只能获取当前文件夹下的所有文件
# path="路径"
# print(os.listdir(path))

# path="D:\PythonWork\sdjh\ceshi"
# os.mkdir(path)
# os.makedirs(path)
# os.rmdir()
# os.rmdir(path)

# os.rename(path) # 重命名

# os.remove()   #删除文件

# import os.path
# os.path模块
# 绝对路径os.path.abspath(a)
# 拼接路径os.path.join(a,b)
# 拆分路径os.path.split(）
# 拆除文件拓展名os.path.splitext()
# 检测是不是文件夹os.path.isdir(i)
# os.path.isfile()
# os.path.exists()检测路径是否存在
# os.path.getsize()获取文件大小
# os.path.dirname()绝对路径
# os.path.basename()当前路径

# 获取指定文件夹下所有的文件，深层获取
import os
# def huoqu(path="D:\PythonWork"):
#     list=os.listdir(path)
#     for i in list:
#         path1=os.path.join(path, i)
#         if os.path.isdir(path1)==False:
#             print(i)
#         else:
#             huoqu(path1)
# huoqu("D:\python3.6")

# str=input()
# str1=""
# for i in str:
#     if str.count(i)>1 and str1.count(i)==0:
#         str1+=i
# print(str1)