import pymysql
import time
from urllib import request

from lxml import etree
from selenium import webdriver

# 定义配置信息
PORT = 3306
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '123456'
DB_NAME = 'pachong'
url = "https://www.guazi.com/wh/buy/o1/"
path = r"C:\Users\lenve\Desktop\瓜子二手车"
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
# 打开浏览器
driver = webdriver.Chrome(chrome_options=options)
# 打开指定网页
driver.get(url)
# driver.find_element_by_xpath("//dl[@class='clearfix'][1]/dd/div[@class='dd-top']/span[@class='a-box']/a[8]").click()
while True:
    # 获取所需爬取的具体内容
    response = etree.HTML(driver.page_source)
    name_list = response.xpath("//ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/h2[@class='t']/text()")
    productive_year_list = response.xpath(
        "//ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/div[@class='t-i']/text()[1]")
    mileage_list = response.xpath(
        "//ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/div[@class='t-i']/text()[2]")
    price_list1 = response.xpath(
        "//ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/div[@class='t-price']/p/text()")
    price_list2 = response.xpath(
        "//ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/div[@class='t-price']/p/span/text()")
    img_url_list = response.xpath("//ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/img/@src")
    # 连接mysql数据库
    conn = pymysql.Connect(host=HOST,
                           user=USER,
                           password=PASSWORD,
                           port=PORT,
                           db=DB_NAME, )
    cursor = conn.cursor()
    label_list = []
    for i in range(len(name_list)):
        str1 = ""
        print(img_url_list[i])
        # 将图片保存至本地
        if len(img_url_list[i]) == 126:
            url1 = img_url_list[i][:-43]
        else:
            url1 = img_url_list[i][:-30]
        print(url1)
        path1 = path + f"\{name_list[i]}.jpg"
        img = request.urlopen(url1).read()
        with open(path1, "wb") as f:
            f.write(img)
        # 将数据存入数据库
        label = response.xpath(
            f"//ul[@class='carlist clearfix js-top']/li[{i}]/a[@class='car-a']/div[@class='t-price']/i/text()")
        for j in label:
            str1 += j
            str1 += ","
        sql = f"INSERT into guazi(name,mileage,productive_year,price,img,label)  VALUES ('{name_list[i]}', '{mileage_list[i]}', '{productive_year_list[i]}', '{price_list1[i]+price_list2[i]}','{img_url_list[i]}','{str1}')"
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    # 执行点击下一页,加载下一页内容
    try:
        driver.find_element_by_xpath("//a[@class='next']").click()
    except:
        # 最后一页无法加载下一页,跳出循环
        break
    time.sleep(3)
# 关闭浏览器
driver.quit()
