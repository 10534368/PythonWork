#-*- coding: utf-8 -*-
# 匿名函数
# 适用情况 当代码只执行一次的时候,只能处理很简单的逻辑
# 如何创建:lambda 拉姆达
import time
import functools
# def mySum(Y,x):
#     return x/Y

# a=lambda x:x+3
# print(a)
# a=lambda x:x+6
# print(a)
# print(mySum)

# h=[]
# for i in range(65,91):
#     name=chr(i)
#     print(name,end="")
#     h.append(name)
#     print(h)
#     h[i-65]=lambda x:x*i
#     print("\r",h[i-65],end="")
#     print(h[i-65](2),end="")
#     time.sleep(1)
# print(h)

# 偏函数
# 可以把一个函数的参数固定住,并生成一个新的函数,不会更改原函数

# mySum2=functools.partial(mySum,2)
# print(mySum2(5))
# a="100"
# print(int(a,base=2))
# base 进制转换可直接写 int(str,n)

# 嵌套函数
# 嵌套定义
def fun1():
    print("a")
    def fun2():
        print("b")

# 回调函数
# 将函数当做参数传递给另一个函数

#装饰器
#   嵌套函数与回调函数相结合

def jishi(f):
    def jisuan(*x):
        n=time.clock()
        f(*x)
        m=time.clock()
        print("程序执行时间:%f"%(m-n))
    return jisuan
@jishi
def fun():
    print("warning")
    time.sleep(2)

# fun()
@jishi
def Fun1(a):
    print("warning")
    time.sleep(a)
# Fun1(1)

@jishi
def 计算器(a,fuhao,b):
    yunsuanfu={"+":"sum", "-":"sub", "*":"ji", "/":"shang", "%":"quyu", "**":"mici", "//":"quzheng"}
    jieguo=""
    for i,j in yunsuanfu.items():
        if fuhao==i:
            jieguo+=str(a)
            jieguo+=i
            jieguo+=str(b)
            n=eval(jieguo)
            print("%s:%d"%(j,n))
            return  ("%s:%d"%(j,n))
    print("没有这个运算方式")
    return ("没有这个运算方式")

# 计算器(1,"+",1)

# map
# 两个参数  函数  list or yuanzu  迭代器
# 依次作用到函数中,作用的结果放到新的序列中

list1=[1,2,3]
def hanshu(a):
    return a**2
list2=list(map(hanshu,list1))
list3=list(map(hanshu,map(hanshu,list1)))
# print(list3)

list4=[5151,1515,5511]
list5=list(map(int,list4))
# print(sum(list5))

import functools
# reduce 参数跟map一样
# 将序列中的数据全部进行累加求和
def fun2(x,y):
    return x+y
n=functools.reduce(fun2,list4)
# print(n)

# capitalize
list6=["soanfiabfkUDSVISB","sdabsdkbkdhvbk","idgdoihiu"]
def fun3(a):
    n=a.upper()
    a1=n[0]+a[1:len(a)]
    return a1
list7=list(map(fun3,list6))
m=functools.reduce(fun2,list7)
print(list7)
print(m)

# filter  过滤数据
list8=[3216,515,1,35,1,65,1,5,31,65,1,65,1,68,465,1,651,474,17,56,1,6,518,16,5,18,64651,6,8,98,1,65,165]
def fun5(s):
    if s%2==0:
        return s
list9=list(filter(fun5,list8))
print(list9)



