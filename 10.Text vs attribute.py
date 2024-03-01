import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
o=webdriver.ChromeOptions()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o, service=s)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

emailbox=driver.find_element(By.ID, "Email")
emailbox.clear()
emailbox.send_keys("abc@yourstore.com")

time.sleep(5)

print("result of text:",emailbox.text)
print("result of get_attribute():",emailbox.get_attribute('value'))

driver.close()



