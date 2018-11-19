import random
import time
import pymysql
import requests
from lxml.html import etree


def get_time():  # 获取当前时间并转化成一定格式
    Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return Time


def pa(url):  # 链接网页返回网页源码
    response = requests.get(url)
    response.encoding = "gbk"
    if response.status_code == 200:
        print(f"{url}连接成功...")
    html_text = etree.HTML(response.text)
    return html_text


def get_bq(n):  # 获取标签(书籍分类)
    url = f"http://www.quanshuwang.com/book_{n}.html"
    text = pa(url)
    t_name_list = text.xpath("//ul[@class='channel-nav-list']/li/a/text()")   # 所有标签---t_name
    t_flag = 0
    for i in t_name_list:
        Time = get_time()
        sql = [f"INSERT into tag(t_name,t_create_time,t_flag)  VALUES ('{i}', '{Time}', '{t_flag}')"]
        add(sql)


def add(sql):  # 将数据存入数据库
    conn = pymysql.Connect(host=HOST,
                           user=USER,
                           password=PASSWORD,
                           port=PORT,
                           db=DB_NAME,
                           charset="utf8",)
    cursor = conn.cursor()
    for i in sql:
        cursor.execute(i)
    conn.commit()
    cursor.close()


def find(sql):  # 查询数据库的数据
    conn = pymysql.Connect(host=HOST,
                           user=USER,
                           password=PASSWORD,
                           port=PORT,
                           db=DB_NAME,
                           charset="utf8",)
    cursor = conn.cursor()
    cursor.execute(sql)
    try:
        result = cursor.fetchall()[0][0]
    except:
        result = False
    conn.commit()
    cursor.close()
    return result


def xpath(text):  # 解析获取书籍基本信息
    img_url = text.xpath("//div[@class='detail']/a[@class='l mr11']/img/@src")[0]# 图片链接---img
    name = text.xpath("//h1/text()")[0]# 小说名---a_title
    jianjie = text.xpath("//div[@class='infoDetail']/div[@id='waa']/text()[1]")[0]# 小说简介---a_content
    author_name = text.xpath("//div[@class='bookDetail']/dl[@class='bookso'][1]/dd/text()")[0]# 作者---username
    category = text.xpath("//a[@class='c009900']/text()")[0]# 类别---a_info
    new_url = text.xpath("//a[@class='reader']/@href")[0]# 章节列表链接
    Time = get_time()
    sql = f"SELECT id FROM author WHERE auth_name='{author_name[1:]}'"
    operator_id = find(sql)
    if operator_id == False:
        sql = [f"INSERT into author(auth_name,a_create_time,a_flag)  VALUES ('{author_name[1:]}', '{Time}', '0')"]
        add(sql)
        sql = f"SELECT id FROM author WHERE auth_name='{author_name[1:]}'"
        operator_id = find(sql)
    sql = f"SELECT id FROM tag WHERE t_name='{category}'"
    a_tag_id = find(sql)
    a_price = random.randint(5, 15)
    sql = [
        f"INSERT into art(a_title,a_img,a_content,a_flag,a_create_time,a_price,a_tag_id,operator_id) VALUES ('{name}', '{img_url}', '{jianjie}', '0','{Time}','{a_price}', '{a_tag_id}', '{operator_id}')"]
    add(sql)
    text = pa(new_url)
    xpath1(text, name)


def xpath1(text, name):  # 解析获取书籍章节信息
    name_urls_list = text.xpath("//div[@class='clearfix dirconone']/li/a/@href")# 章节链接列表---content
    name_list = text.xpath("//div[@class='clearfix dirconone']/li/a/text()")# 章节名字列表---title
    sql = f"SELECT id FROM art WHERE a_title='{name}'"
    art_id = find(sql)
    sql_s = []
    for i in range(len(name_urls_list)):
        Time = get_time()
        sql = f"INSERT into art_chapter(title,content,create_time,art_id) " \
              f" VALUES ('{name_list[i]}', '{name_urls_list[i]}', '{Time}', '{art_id}')"
        sql_s.append(sql)
    add(sql_s)


PORT = 3306
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '123456'
DB_NAME = 'wh1804_django'
n = 2862
# get_bq(n)
while True:
    url = f"http://www.quanshuwang.com/book_{n}.html"
    n += 1
    text = pa(url)
    try:
        xpath(text)
    except:
        pass