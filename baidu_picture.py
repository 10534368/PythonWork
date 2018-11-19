from selenium import webdriver
from lxml import etree
import time

url="https://image.baidu.com/"
a=webdriver.Chrome()
a.get(url)
a.find_element_by_xpath("//input[@id='kw']").send_keys("动漫")
a.find_element_by_xpath("//span[@class='s_search']").click()
time.sleep(7)
n=0
while True:
    print(a.page_source)
    result=etree.HTML(a.page_source).xpath("//img[@class='main_img img-hover']/@src")
    table=etree.HTML(a.page_source).xpath("//img[@class='main_img img-hover']")[0]
    content2 = etree.tostring(table)
    print(content2)
    print(etree.HTML(a.page_source).xpath("//img[@class='main_img img-hover']"))
    print(len(result))
    # for i in result:
        # print(i)
    m = n + 500
    a.execute_script(f"window.scrollTo({n},{m})")
    n += 500
    time.sleep(3)
