import os
from urllib import request

from bs4 import BeautifulSoup



def fun(url, n=0, p=list()):
    URL = request.urlopen(url)
    m = URL.read()
    soup = BeautifulSoup(m, 'html.parser', from_encoding='utf-8')
    if URL.getcode() == 200:
        print("连接成功...")
    links = soup.find_all('img')
    links1 = soup.find_all('div')
    links2 = soup.find_all('h1')
    path = r"C:\Users\lenve\Desktop\img\%s" % (links2[0].get_text())
    istrue = os.path.exists(path)
    if not istrue:
        os.makedirs(path)
    for link1 in links1:
        try:
            if link1['class'] == ['tpl-img-title']:
                p.append(link1.get_text())
        except:
            pass
    print(len(p))
    for link in links:
        try:
            if link['class'] == ['lazy']:
                str2 = link['data-original'][:-6]
                str1 = request.urlopen(str2).read()
                try:
                    path = r"C:\Users\lenve\Desktop\img\%s\img%d_%s.jpg" % (links2[0].get_text(), n, p[n])
                    istrue = os.path.exists(path)
                    if not istrue:
                        f = open(path, "wb")
                        f.write(str1)
                        f.close()
                    print('\r%d-%s' % (n, path), end='')
                    n += 1
                except:
                    pass
        except:
            pass
    links2 = soup.find_all('a')
    for link2 in links2:
        try:
            if link2['class'] == ['downPage']:
                print()
                fun(link2['href'], n, p)
        except:
            pass


url = 'http://588ku.com/bj-zt/1969.html'
fun(url)
