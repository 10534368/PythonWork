#-*- coding: utf-8 -*-
def hanshu():
    print("ojbk")
if __name__=="__main__":
    print("你看不到我")

def qiuhe(*args):
    num=0
    for i in args:
        num+=i
    print(num)
    return num