import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O, service=S)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("RakesH")
time.sleep(5)
