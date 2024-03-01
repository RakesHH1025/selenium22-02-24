import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O, service=S)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
alert=driver.switch_to.alert


time.sleep(5)
alert.accept()


driver.quit()
