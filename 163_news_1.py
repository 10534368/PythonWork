import hashlib

import pymysql
import requests
from lxml import etree


def create_pwd_md5(str1):
    h1 = hashlib.md5()
    h1.update(str1.encode(encoding="utf-8"))
    return h1.hexdigest()


def add(sql):  # 将数据存入数据库
    for i in sql:
        try:
            cursor.execute(i)
        except Exception as e:
            print(e)
    conn.commit()


def find(sql):  # 查询数据库的数据
    cursor.execute(sql)
    try:
        result = cursor.fetchall()[0][0]
    except:
        result = False
    return result


def pa(url):  # 链接网页返回网页源码
    response = requests.get(url)
    response.encoding = "gbk"
    html_text = etree.HTML(response.text)
    return html_text


def main(url_list, tag):
    for url in url_list:
        print(f"\r{url}", end="")
        html_text = pa(url)
        content_list = html_text.xpath("//div[@id='epContentLeft']/div[@class='post_body']/div[@id='endText']/p")
        if content_list == []:
            continue
        title = html_text.xpath("//h1/text()")[0]  # 标题
        sql = f"SELECT * FROM news WHERE title='{pymysql.escape_string(title)}'"
        result = find(sql)
        if result != False:
            continue
        hash_id = create_pwd_md5(title)  # hash_id
        try:
            img_url = html_text.xpath("//div[@id='endText']/p/img/@src[1]")[0]
        except:
            img_url = 0
        sql = f"SELECT type_id FROM kind WHERE type='{tag}'"
        type_id = find(sql)
        #  标签id
        update_time = html_text.xpath("//div[@class='post_time_source']/text()")[0]  # 更新时间
        for num in range(len(update_time)):
            if update_time[num] == "2":
                update_time = update_time[num:]
                break
        update_time = update_time[:19]
        try:
            article_source = html_text.xpath("//a[@id='ne_article_source']/text()")[0]  # 文章来源
        except:
            article_source = "/"
        try:
            editor = html_text.xpath("//span[@class='ep-editor']/text()")[0]  # 责任编辑
        except:
            editor = "/"
        sql_list = [
            f"INSERT into news(hash_id,title,type_id,img_url,author,news_from,create_time,store_up_num,comment_num,click_num) VALUES ('{hash_id}','{pymysql.escape_string(title)}', '{type_id}','{img_url}', '{editor}', '{article_source}','{update_time}','0', '0','0')"]
        add(sql_list)
        sql_list = []
        for content in content_list:
            if content.xpath("text()") == [] and content.xpath("img/@src") == []:
                continue
            elif content.xpath("text()") != []:
                text = content.xpath("text()")
                sql_list.append(
                    f"INSERT into news_content(hash_id,title,type) VALUES ('{hash_id}','{pymysql.escape_string(text[0])}', 'p')")
            else:
                text = content.xpath("img/@src")
                sql_list.append(
                    f"INSERT into news_content(hash_id,title,type) VALUES ('{hash_id}','{pymysql.escape_string(text[0])}', 'img')")
        if sql_list == []:
            continue
        add(sql_list)


def login(url):
    response = requests.get(url, headers=headers)
    response.encoding = "gb2312"
    tree = etree.HTML(response.text)
    tag_url_list = tree.xpath("//div[@class='area areabg1']/div/div[@class='more']/a/@href")
    # 爬取分类标签
    tag_list = tree.xpath("/html/body/div[@class='area areabg1']/div/h2/text()")
    _tag_list = tag_list[12:15]
    # for i in _tag_list:
    #     sql = [f"INSERT into kind(type)  VALUES ('{i}')"]
    #     add(sql)
    _tag_url_list = tag_url_list[12:15]
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
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '123456'
# HOST = '47.104.111.111'
# USER = 'wang'
# PASSWORD = '309609'
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
