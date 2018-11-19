from bs4 import BeautifulSoup
import pymysql
import requests

def GeYan():
    url = "https://www.geyanw.com"
    URL = requests.get(url)
    URL.encoding="GBK"
    soup = BeautifulSoup(URL.text, 'html.parser')
    if URL.status_code == 200:
        print("连接成功...")
    links1 = soup.find_all("div")
    links2 = []
    for link1 in links1:
        try:
            if link1["id"] == "toplink" or link1["id"] == "nav" or link1["id"] == "container" or link1[
                "id"] == "p_left" or link1["id"] == "p_right":
                links2 += link1.find_all("a")
        except:
            pass
    PORT = 3306
    HOST = '127.0.0.1'
    USER = 'root'
    PASSWORD = '123456'
    DB_NAME = 'pachong'
    conn = pymysql.Connect(host=HOST,
                           user=USER,
                           password=PASSWORD,
                           port=PORT,
                           db=DB_NAME,
                           charset='GBK')
    cursor = conn.cursor()
    path = r"C:\Users\lenve\Desktop\img"
    for link2 in links2:
        url1 = url + link2["href"]
        print(link2.get_text())
        print(url1)
        sql = f"INSERT into geyanw(title,url)  VALUES ('{link2.get_text()}', '{url1}') "
        cursor.execute(sql)
    conn.commit()
    cursor.close()


GeYan()
