from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=O, service=S)

# mywait=WebDriverWait(driver,10)  #explicit wait declaration # basic

mywait=WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException
                                                                     ])

driver.get("https://www.google.co.in/")
driver.maximize_window()

search_box=driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()

