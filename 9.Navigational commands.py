from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

serv_obj=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
object=webdriver.ChromeOptions()
object.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=object, service=serv_obj)

driver.get("https://www.snapdeal.com")
time.sleep(1)

driver.maximize_window()

driver.get("http://www.amazon.com")
time.sleep(1)

driver.back()
time.sleep(1)

driver.forward()
time.sleep(1)

driver.refresh()
time.sleep(1)

driver.quit()
