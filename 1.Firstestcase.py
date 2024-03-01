import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
input_box=driver.find_element(By.NAME, "Email")
input_box.clear()
input_box.send_keys("admin@yourstore.com")
password=driver.find_element(By.ID, "Password")
password.clear()
password.send_keys("admin")
driver.find_element(By.CLASS_NAME, "button-1").click()
time.sleep(2)

exp_title="Admin area demo"
actual_title="Admin area demo"
if actual_title==exp_title:
    print("Test case passed")
else:
    print("Test case failed")

driver.close()
