# 文件操作
# 读 写
# 读  打开文件  读取  关闭
# open(name,模式，)
# r rb r+ w wb w+ a a+
# path=r"C:\Users\lenve\Desktop\待定.txt"
# f=open(path,"r")
# print(f.readlines())
# f.close()

# readline  读取一行  readlines 读取多行，并将每一行的内容添加到列表中
# path=r"C:\Users\lenve\Desktop\wallpaper_201707(1920x1080).txt"
# f=open(path,"rb")
# print(f.read().decode())
# f.close()

#  写  打开文件  写入 关闭
# path=r"C:\Users\lenve\Desktop\待定.txt"
# f=open(path,"a+")
# f.write("明天考试")
# f.close()

# path=r"C:\Users\lenve\Desktop\a\待定.txt"
# f=open(path,"r")
# str=f.read()
# path1=r"C:\Users\lenve\Desktop\b\2.txt"
# f1=open(path1,"w")
# f1.write(str)
# f.close()
# f1.close()

# path=r"C:\Users\lenve\Desktop\a\ScreenShot2018_0715_003315582.jpg"
# f=open(path,"rb")
# str=f.read()
# path1=r"C:\Users\lenve\Desktop\b\清泉流响.jpg"
# f1=open(path1,"wb")
# f1.write(str)
# f.close()
# f1.close()

# 一个PY文件就是一个模块
# import 导入模块
# 只导入一个函数
# from Tool import fun
# fun()
# print(__name__)
# if __name__=="__main__":
#     pass

# import Tool
# # from Tool import hanshu
# Tool.hanshu()

# Tool.qiuhe(123,456,789)
# a=Tool.qiuhe(123,456,789)

# 系统内置模块
# 自定义模块   自己写的
# 第三方模块    别人写的

# bao

# import baolegebao.Tool
# baolegebao.Tool.mokuai()

# 时间模块 time
# 从1970年1月1日零点开始到现在
# 时间戳
import time
# print(time.time())
# print(time.localtime())#获取本地时间 存在元组中
# print(time.ctime())
# tuple1=time.localtime()
# str=time.asctime(tuple1)#元组转字符串
# print(time.mktime(tuple1))转时间戳
# print(time.gmtime())时间戳转位元组
# print(time.clock())
# 3.7758147736304646e-07
# print(time.strptime("Thu Jul 19 16:21:38 2018"))
# time.sleep(2) 休息两秒
# print(time.clock()) 检测程序运行多久

# %Y年 %m月  %d天  %H时   %M分  %S秒

# 栈 队列
# 压栈
# 弹栈
# python数据结构里边没有栈

import collections,queue
# 创建队列
# a=queue.Queue(3)
# a.put("a")
# a.put("b")
# a.put("c")
# print(a.get())
# print(a.get())
# print(a.get())

# 二维列表 (列表嵌套列表)
# list1=[1,2,3]
# list2=[4,5,6]
# list3=[list1,list2]
# print(list1[2])
# print(list2[1])
# print(list3[1][1])
# list4=[[1,2,["a","b"]]]
# print(list4[0][2][1])

# list4=["a","b"]
# list1=[1,2,3]
# list1.append(list4)
# list2=list1
# list3=list1.copy()
# print(list3)
# list2[0]=10
# list2[-1].append("c")
# print(list1)
# print(list2)
# print(list3)

import copy
# copy.deepcopy