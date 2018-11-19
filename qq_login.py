from selenium import webdriver
import time
import pytesseract
from PIL import Image
import matplotlib

# text=pytesseract.image_to_string(Image.open(r"D:\PythonWork\6.png"),lang="eng")
# text=text.replace(" ","")
# print(text)
# exit()
url="https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=https%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=https%3A//z.qzone.com/download.html&pt_no_auth=0"
driver=webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath("//a[@id='switcher_plogin']").click()
driver.find_element_by_xpath("//input[@id='u']").send_keys("3118309798")
driver.find_element_by_xpath("//input[@id='p']").send_keys("****")
driver.find_element_by_xpath("//input[@id='login_button']").click()
time.sleep(5)
driver.quit()