import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O, service=S)
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

search_box=driver.find_element(By.NAME, "q")
# time.sleep(5)
search_box.send_keys("Selenium")
search_box.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
time.sleep(10)

driver.quit()