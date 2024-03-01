from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

sliders=driver.find_elements(By.CLASS_NAME, "nivo-main-image")
print(len(sliders))

links=driver.find_elements(By.TAG_NAME, "a")
print(len(links))

driver.close()

