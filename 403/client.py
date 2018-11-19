#-*- coding: utf-8 -*-
# 客户端的代码 TCP协议传输
# 1 创建socket对象(指定IP地址的方式,传输协议,)
# 2 建立连接 (指定IP地址和端口号)
# 3 发送数据
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.58.49", 9000))
while True:
    data1=input("说话")
    s.send(data1.encode())
    if data1=="拜拜":
        break
    data=s.recv(1024)
    print(data.decode())
    if data.decode()=="拜拜":
        break
s.close()