#-*- coding: utf-8 -*-
import socket

str = "1_lbt4_10#32499#002481627512#0#0#0:1289671407:赛丽亚:克鲁敏:288:你好啊,我叫赛丽亚"


for i in range(256):
    ip = "192.168.58.1"
    print(ip)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.connect((ip,2425))
    udp.send(str.encode("gbk"))