import hashlib
from urllib import request

import pymysql
import requests
from bs4 import BeautifulSoup
from lxml import etree


def create_pwd_md5(str1):
    h1 = hashlib.md5()
    h1.update(str1.encode(encoding="utf-8"))
    return h1.hexdigest()


def add(sql):  # 将数据存入数据库
    for i in sql:
        try:
            cursor.execute(i)
        except:
            pass
    conn.commit()


def find(sql):  # 查询数据库的数据
    cursor.execute(sql)
    try:
        result = cursor.fetchall()[0][0]
    except:
        result = False
    return result


def main(url_list, tag):
    for i in range(len(url_list)):
        print(f"\r{i}-{url_list[i]}", end="")
        data = request.Request(url=url_list[i], headers=headers)
        try:
            html = request.urlopen(data).read()
        except:
            continue
        soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')
        try:
            # 爬取正文
            zheng_wen_list = soup.find(id='endText').find_all('p')
            zheng_wen = ""  # 正文
            for i in zheng_wen_list:
                zheng_wen += str(i)
            # 爬取其他内容
            tree = etree.HTML(str(soup))
            try:
                img_url = tree.xpath("//div[@id='endText']/p/img/@src[1]")[0]
            except:
                img_url = 0
            title = tree.xpath("//h1/text()")[0]  # 标题
            sql = f"SELECT * FROM news WHERE title='{title}'"
            result = find(sql)
            if result != False:
                continue
            hash_id = create_pwd_md5(title)  # hash_id
            sql = f"SELECT type_id FROM kind WHERE type='{tag}'"
            type_id = find(sql)
            #  标签id
            update_time = tree.xpath("//div[@class='post_time_source']/text()")[0][:-5]  # 更新时间
            for i in range(len(update_time)):
                if update_time[i] == "2":
                    update_time = update_time[i:]
                    break
            article_source = tree.xpath("//a[@id='ne_article_source']/text()")[0]  # 文章来源
            editor = tree.xpath("//span[@class='ep-editor']/text()")[0]  # 责任编辑
            sql_list = [
                f"INSERT into news(hash_id,title,content,type_id,img_url,author,news_from,create_time,store_up_num,comment_num,click_num) VALUES ('{hash_id}','{title}','{zheng_wen}', '{type_id}','{img_url}', '{editor}', '{article_source}','{update_time}','0', '0','0')"]
            add(sql_list)
        except:
            pass


def login(url):
    response = requests.get(url, headers=headers)
    response.encoding = "gb2312"
    tree = etree.HTML(response.text)
    tag_url_list = tree.xpath("//div[@class='area areabg1']/div/div[@class='more']/a/@href")
    # 爬取分类标签
    tag_list = tree.xpath("/html/body/div[@class='area areabg1']/div/h2/text()")
    _tag_list = tag_list[1:9] + tag_list[11:15]
    # for i in _tag_list:
    #     sql = [f"INSERT into kind(type)  VALUES ('{i}')"]
    #     add(sql)
    _tag_url_list = tag_url_list[1:9] + tag_url_list[11:15]
    for i in range(len(_tag_url_list)):
        response = requests.get(_tag_url_list[i])
        response.encoding = "gb2312"
        tree = etree.HTML(response.text)
        news_url_list = tree.xpath("//div[@class='area areabg1']//div[@class='tabBox']//table//a/@href")
        news_url_list = list(set(news_url_list))
        print(len(news_url_list), _tag_list[i])
        main(news_url_list, _tag_list[i])
        print("")


PORT = 3306
HOST = '47.104.111.111'
USER = 'wang'
PASSWORD = '309609'
DB_NAME = 'flask_news'
conn = pymysql.Connect(host=HOST,
                       user=USER,
                       password=PASSWORD,
                       port=PORT,
                       db=DB_NAME,
                       charset="utf8", )
cursor = conn.cursor()
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = "http://news.163.com/rank/"
login(url)
cursor.close()