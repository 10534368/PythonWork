from selenium import webdriver
from lxml import etree

img_urls=[]
url="http://books.toscrape.com/"
a=webdriver.Chrome()
a.get(url)
while True:
    text = a.page_source
    for i in etree.HTML(text).xpath("//img[@class='thumbnail']/@src"):
        img_urls.append(url+i[3:]) if len(img_urls)>20 else img_urls.append(url+i)
    print(f"\r{a.current_url},{len(img_urls)}",end="")
    a.find_element_by_xpath("//li[@class='next']/a").click()
n=0
while True:
    result=etree.HTML(a.page_source).xpath("//img[@class='main_img img-hover']/@src")
    print(len(result))
    for i in result:
        print(i)
    m = n + 500
    a.execute_script(f"window.scrollTo({n},{m})")
    n += 500
    time.sleep(3)