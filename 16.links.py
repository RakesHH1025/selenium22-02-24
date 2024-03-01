from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O,service=S)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "downloads").click()

alllinks=driver.find_elements(By.XPATH, "//a")
print(len(alllinks))

for i in alllinks:
    print(i.text)

time.sleep(3)
driver.quit()
