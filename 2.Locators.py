import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()



# id & name locators
#driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.CLASS_NAME, "button-1").click()

# linktext & partial linktext
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
# time.sleep(5)
driver.close()