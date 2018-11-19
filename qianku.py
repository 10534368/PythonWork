from bs4 import BeautifulSoup
from urllib import request
import os

def fun(url,n=0,p=list(),path=r"C:\Users\lenve\Desktop\mp4"):
    URL= request.urlopen(url)
    soup = BeautifulSoup(URL.read(), 'html.parser', from_encoding='utf-8')
    print(soup)
    if URL.getcode()==200:
        print("连接成功...")
    links = soup.find_all('video')
    print(links)
    links1 = soup.find_all('a')
    if path==r"C:\Users\lenve\Desktop\mp4":
        links2 = soup.find_all('title')
        path = r"C:\Users\lenve\Desktop\mp4\%s" % (links2[0].get_text())
    path1=path
    istrue = os.path.exists(path)
    if not istrue:
        os.makedirs(path)
    for link1 in links1:
        try:
            if link1['class'] == ['title']:
                p.append(link1.get_text())
        except:
            pass
    print(len(p))
    for link in links:
        try:
            path2 = path + "\mp4_%d_%s.mp4" % (n, p[n])
            istrue = os.path.exists(path2)
            if not istrue:
                str1 = request.urlopen(link['src']).read()
                f = open(path2, "wb")
                f.write(str1)
                f.close()
            print('\r%d-%s' % (n, path2), end='')
            n += 1
        except:
            pass
    for link1 in links1:
        try:
            if link1['class'] == ['downPage']:
                print("\n下一页")
                fun(link1['href'],n,p,path1)
        except:
            pass

fun(url='http://588ku.com/video/shipin/')