#-*- coding: utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.58.49",1000))
while True:
    data,add=s.recvfrom(1024)
    print(data.decode(),"来自于",add)