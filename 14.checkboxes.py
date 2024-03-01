from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O, service=S)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


#select one checkbox
driver.find_element(By.ID, "sunday").click()

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

print(len(checkboxes))

# for i in elements:
#     i.click()

#select all checkboxes

# for checkbox in checkboxes:
#     checkbox.click()

for checkbox in checkboxes:
    weekname=checkbox.get_attribute('id')
    if weekname=="monday" and weekname=="sunday":
        checkbox.click()

#6) clearing all the check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

time.sleep(2)

driver.close()
