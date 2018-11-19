from multiprocessing import Pool

import pymysql
import requests
from lxml.html import etree


def Book_Toscrape(html_text, url):
    img_urls = html_text.xpath("//img[@class='thumbnail']/@src")
    books_name = html_text.xpath("//img[@class='thumbnail']/@alt")
    prices = html_text.xpath("//p[@class='price_color']/text()")
    star_rating = html_text.xpath("//article[@class='product_pod']/p/@class")
    availabilitys = html_text.xpath("//p[@class='instock availability']/text()[2]")
    details_urls = html_text.xpath("//div[@class='image_container']/a/@href")
    PORT = 3306
    HOST = '127.0.0.1'
    USER = 'root'
    PASSWORD = '123456'
    DB_NAME = 'pachong'
    conn = pymysql.Connect(host=HOST,
                           user=USER,
                           password=PASSWORD,
                           port=PORT,
                           db=DB_NAME, )
    cursor = conn.cursor()
    for i in range(len(details_urls)):
        if url == "http://books.toscrape.com/":
            details_url = url + details_urls[i]
            img_url = url + img_urls[i]
        else:
            details_url = "http://books.toscrape.com/catalogue/" + details_urls[i]
            img_url = "http://books.toscrape.com/" + img_urls[i][3:]
        for n in books_name[i]:
            if n == '"':
                books_name[i] = books_name[i].replace(n, "'")
        print(books_name[i])
        availability = availabilitys[i][14:-6]
        print(img_url)
        print(details_url)
        sql = f'INSERT into book_toscrape(book_title,img_url,price,star_rating,availability,details_url) VALUES ("{books_name[i]}", "{img_url}", "{prices[i][1:]}", "{star_rating[i][12:]}","{availability}","{details_url}") '
        cursor.execute(sql)
    conn.commit()
    cursor.close()


url = "http://books.toscrape.com/"

if __name__ == '__main__':
    pool = Pool(processes=4)
    results = []
    url_list = [url]
    for i in url_list:
        response = requests.get(i)
        response.encoding = "utf8"
        if response.status_code == 200:
            print(f"{i}连接成功...")
        html_text = etree.HTML(response.text)
        next_url = html_text.xpath("//li[@class='next']/a/@href")
        result = pool.apply_async(Book_Toscrape(html_text, i))
        if next_url != []:
            if i == "http://books.toscrape.com/":
                url1 = url + next_url[0]
            else:
                url1 = "http://books.toscrape.com/catalogue/" + next_url[0]
            url_list.append(url1)
        else:
            exit()
    pool.close()
    pool.join()
