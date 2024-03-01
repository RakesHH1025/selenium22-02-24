from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
object=webdriver.ChromeOptions()
object.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=object, service=serv)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

# or
# driver.find_element(By.XPATH, "//input[@name='q' or @id='small-searchterms']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# and
# driver.find_element(By.XPATH, "//input[@placeholder='Search store' and @name='q']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# contains()
driver.find_element(By.XPATH, "//input[contains(@id,'small-searchterms')]").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#starts-with()
driver.find_element(By.XPATH, "//a[starts-with(text(), 'Search')]").click()

# driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()

time.sleep(5)
driver.close()


