from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

search_box=driver.find_element(By.ID, "small-searchterms")
print(search_box.is_displayed())
print(search_box.is_enabled())

rd_male=driver.find_element(By.ID, "gender-male")
print(rd_male.is_selected())



driver.close()