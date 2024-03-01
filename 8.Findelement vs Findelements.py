from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#######  find_element() - Returns single webelement
#1)Locator matching with single webelement
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.close()

#2) Locator matching with multiple webelements
# elements=driver.find_elements(By.XPATH, By.XPATH, "//div[@class='footer']//a")

#3) Element not available then throw NoSuchElementException
# login_element=driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()

#######   find_elements() - Returns multiple webElements
#1)Locator matching with single webelement
searchelement=driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(len(searchelement))
searchelement[0].send_keys("Apple MacBook Pro 13-inch")

#2) Locator matching with multiple webelements
elements=driver.find_elements(By.TAG_NAME, "a")
print(len(elements))

for ele in elements:
    print(ele.text)

#3 Element not available - zero
elements=driver.find_elements(By.LINK_TEXT,"Log")
print("elementws returend:",len(elements))



driver.close()
