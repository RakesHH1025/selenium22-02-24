import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
o=webdriver.ChromeOptions()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o,service=s)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
time.sleep(5)
alerts=driver.switch_to.alert
# alerts.accept()
alerts.dismiss()
time.sleep(5)
driver.quit()