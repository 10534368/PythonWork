from selenium import webdriver
from lxml import etree

url = "https://www.fpzw.com/xiaoshuo/12/12027/3756819.html"
path = r"C:\Users\lenve\Desktop\龙魂剑士.txt"
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.GBK')
options.add_argument(
    'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
a = webdriver.Chrome(chrome_options=options)
a.get(url)
while True:
    title = etree.HTML(a.page_source).xpath("//h2/text()")
    text = etree.HTML(a.page_source).xpath("//p[@class='Text']/text()")
    print(a.current_url, title[0])
    with open(path, "a+", encoding='utf-8') as f:
        f.write(title[0] + "\n" + "\n")
        for i in range(len(text)):
            if i < 2:
                pass
            elif i == len(text) - 1:
                f.write(text[i][4:-7] + "\n")
            else:
                f.write(text[i][4:] + "\n")
        f.write("\n")
    try:
        a.find_element_by_xpath("//div[@class='thumb']/a[5]").click()
    except:
        print("Success")
        a.quit()
        exit()
