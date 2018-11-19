from selenium import webdriver
from PIL import Image

PORT = 3306
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '123456'
DB_NAME = 'wh1804_django'

n=f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset=utf8"

broswer = webdriver.Chrome()
broswer.get("http://www.baidu.com")
broswer.save_screenshot(r'photo.png')
baidu = broswer.find_element_by_id('su')
broswer.quit()
left = baidu.location['x']
top = baidu.location['y']
elementWidth = baidu.location['x'] + baidu.size['width']
elementHeight = baidu.location['y'] + baidu.size['height']
picture = Image.open(r'photo.png')
picture = picture.crop((left, top, elementWidth, elementHeight))
picture.save(r'photo2.png')
#截取指定元素快照