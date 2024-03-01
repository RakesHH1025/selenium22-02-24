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

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()