from selenium import webdriver
import time


a=webdriver.Chrome()
a.get("http://stu.1000phone.net")
a.find_element_by_name("Account").send_keys(input())
a.find_element_by_name("PassWord").send_keys(input())
a.find_element_by_xpath("//button[@class='width-100 pull-right btn btn-sm btn-primary']").click()
a.find_element_by_xpath("//li[5]/a[@class='dropdown-toggle']").click()
a.find_element_by_xpath("//a[@class='btn btn-xs btn-success']").click()
for i in range(1,14):
    a.find_element_by_xpath(f"//tbody[@id='topic']/tr[{i}]/td[3]/label[1]").click()
a.find_element_by_xpath("//textarea[@id='YIUrmG']").send_keys(" ")
a.find_element_by_xpath("//textarea[@id='Nf8QDS']").send_keys(" ")
a.find_element_by_xpath("//button[@id='addstudent']").click()
time.sleep(5)
# a.save_screenshot("1.png")
a.quit()

