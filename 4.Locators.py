import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag & id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("770212456")
# driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("12654898")
#
#tag & class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("770212456")
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("12654898")

#tag & attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid='royal_email']").send_keys("770212456")
# driver.find_element(By.CSS_SELECTOR, "[data-testid='data-testid']").send_keys("12654898")

#tag class attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[name='email']").send_keys("770212456")
# driver.find_element(By.CSS_SELECTOR, "c.inputtext[id='pass']").send_keys("12654898")

time.sleep(5)
driver.close()
