import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
o=webdriver.ChromeOptions()
o.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=o, service=s)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("RakesHH")
time.sleep(5)

driver.quit()

# innerframe=driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
# driver.switch_to.frame(0)
# driver.switch_to.frame(innerframe)
# driver.switch_to.frame(2)