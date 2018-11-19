import time

from selenium import webdriver

a=webdriver.Chrome()
a.get("http://127.0.0.1:8000")
js='window.open("https://fanyi.baidu.com");'
a.execute_script(js)
# a.get("https://fanyi.baidu.com")
a.switch_to_window(a.window_handles[0])
a.find_element_by_xpath("//li[1]/a[@class='curlink']").click()#点击登录
a.find_element_by_xpath("//p[1]/input[@id='id_username']").send_keys("lvyunpeng")
a.find_element_by_xpath("//p[2]/input[@id='id_password']").send_keys("123456")
a.find_element_by_xpath("//label[1]/input[@class='button']").click()
time.sleep(5)
a.find_element_by_xpath("//div[@class='col-md-3'][1]/div[@class='artlist text-center']/a[@class='btn btn-primary']").click()
a.switch_to_window(a.window_handles[1])
for handle in a.window_handles:#方法二，始终获得当前最后的窗口
    a.switch_to_window(handle)
    time.sleep(2)
a.find_element_by_xpath("//a[@class='btn primary btn-success']").click()
time.sleep(5)

# a.save_screenshot("1.png")
a.quit()