#-*- coding: utf-8 -*-
import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    s.sendto("你好啊,我叫赛丽亚".encode(),("192.168.58.49",1000))
    time.sleep(2)