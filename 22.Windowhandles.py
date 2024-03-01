from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(options=O, service=S)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

windowid=driver.current_window_handle
print(windowid)

driver.find_element(By.XPATH, "//a[contains(text(),'open cart')]").click()


driver.quit()