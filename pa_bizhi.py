import os
from urllib import request

from lxml import etree
from selenium import webdriver

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = "http://www.win4000.com/wallpaper_detail_152656.html"
path = r"C:\Users\lenve\Desktop\壁纸"
istrue = os.path.exists(path)
if not istrue:
    os.makedirs(path)
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.utf-8')
a = webdriver.Chrome(chrome_options=options)
a.get(url)
while True:
    img_url_list = etree.HTML(a.page_source).xpath(
        "//div[@class='main-wrap']/div[@class='scroll-img-cont']/ul[@id='scroll']/li/a/img/@data-original")
    title = etree.HTML(a.page_source).xpath("//h1/text()")[0]
    n=1
    for img_url in img_url_list:
        new_img_url = img_url[:-11] + "_1366_768" + img_url[-4:]
        print(new_img_url)
        str1 = request.urlopen(request.Request(url=new_img_url, headers=headers)).read()
        path2 = path + fr"\{title}_{n}.jpg"
        with open(path2, "wb") as f:
            f.write(str1)
        n += 1
    try:
        a.find_element_by_xpath("//span[@class='group-next']/a").click()
    except:
        print("Success")
        a.quit()
