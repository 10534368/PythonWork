# coding=utf-8
from urllib import request  # Mac

from bs4 import BeautifulSoup
# from urllib.request import Request, urlopen # Win
from lxml import etree

html = request.urlopen('https://news.163.com/18/1115/10/E0L8BNJR000189FH.html').read()
# html = u'''
# <html>
#     <p>发给iuwgfisf</p>
#     <span id="chTitle">退火对Nb<sub>2</sub>O<sub>5</sub>薄膜的折射率和厚度的影响</span>
# </html>
# '''
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# print(html)
tree = etree.HTML(str(soup))

strs = tree.xpath( "//div[@id='epContentLeft']/div[@class='post_body']/div[@id='endText']/p")
for i in strs:
    stre = i.xpath("text()")
    print(stre)
# strs = (etree.tostring(strs)) # 不能正常显示中文
# strs = (etree.tostring(strs, pretty_print = True, method = "html")) # 可以正常显示中文
print (strs)
print(len(strs))
print(type(strs))
# 结果为：退火对Nb
# content1 = tree.xpath("//p")[0]
# print(str(etree.tostring(content1,encoding = "utf-8", pretty_print=True, method="html"))[2:-1])

# 结果为：退火对Nb<sub>2</sub>O<sub>5</sub>薄膜的折射率和厚度的影响
# table = tree.xpath("//span[@id='chTitle']")[0]
# print(table)

# content2 = str(tostring(table))[2:-1]
# print(content2)
# print(HTMLParser.unescape(content2)[19:-8])
