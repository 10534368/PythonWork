# -*- coding: utf-8 -*-
# 排序  冒泡排序  选择排序
def choice(L):
    for i in range(1,len(L)):
        if int(L[i])<int(L[0]):
            L[0],L[i]=L[i],L[0]
    if len(L)==2:
        return L[0:]
    L[1:]=choice(L[1:])
    return  L

def bubble(L):
    for i in range(len(L)-1):
        if int(L[i+1])<int(L[i]):
            L[i],L[i+1]=L[i+1],L[i]
    if len(L)==2:
        return L[:len(L)]
    L[:len(L)-1]=bubble(L[:len(L)-1])
    return L

list=[90,2,5,100,-2,-1,100,-2,5]
print(choice(list))
print(bubble(list))
