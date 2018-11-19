#-*- coding: utf-8 -*-
import socket
n=socket.gethostname()
print(n)
ip=socket.gethostbyname(n)
print(ip)
# netstat -aon
def jsq(shizi):
    try:
        n=eval(shizi)
    except ZeroDivisionError as e:
        print("除数不能为零")
    except:
        print("运算方式不存在")
    else:
        print(n)
while True:
    jsq(input("请输入一个式子(例如:1+1):"))

