import time
from selenium import webdriver
from lxml import etree

url = "https://sou.zhaopin.com/?jl=489&kw=python&kt=3"
path = r"C:\Users\lenve\Desktop\智联招聘-python.txt"
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
a = webdriver.Chrome(chrome_options=options)
a.get(url)
time.sleep(2)
a.find_element_by_xpath("//li[@class='listsort__uls__item'][3]/a[@class='listsort__uls__item__a']").click()
time.sleep(10)
while True:
    title = etree.HTML(a.page_source).xpath("//div[@class='contentpile__content__wrapper__item__info']")
    text = etree.HTML(a.page_source).xpath("//a/span[@class='contentpile__content__wrapper__item__info__box__jobname__title']")
    print(a.current_url, title[0],text)
    try:
        try:
            a.find_element_by_xpath("//button[@class='btn soupager__btn'][2]").click()
        except:
            a.find_element_by_xpath("//button[@class='btn soupager__btn']").click()
    except:
        print("Success")
        a.quit()