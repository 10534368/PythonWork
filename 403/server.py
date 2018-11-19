#-*- coding: utf-8 -*-
# 绑定端口号和ip地址
# 监听
#接受请求 接入过来的客户端对象
          # 地址的各种信息
#接收数据
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.58.49",9000))
s.listen(5)
client,add=s.accept()
while True:
    data=client.recv(2048)
    print(data.decode())
    if data.decode()=="拜拜":
        break
    data1=input("输入回话")
    client.send(data1.encode())
    if data1=="拜拜":
        break
s.close()