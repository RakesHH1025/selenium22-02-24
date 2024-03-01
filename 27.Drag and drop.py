from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O, service=S)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act=ActionChains(driver)

rome_ele=driver.find_element(By.ID,"box6")
italy_ele=driver.find_element(By.ID,"box106")

Washington_ele=driver.find_element(By.ID, "box3")
U=driver.find_element(By.ID, "box103")

Copenhagen_ele=driver.find_element(By.ID, "box4")
norway=driver.find_element(By.ID, "box104")

Seoul_ele=driver.find_element(By.ID, "box5")
south=driver.find_element(By.ID, "box105")

Madrid_ele=driver.find_element(By.ID, "box7")
spain=driver.find_element(By.ID, "box107")

Oslo_ele=driver.find_element(By.ID, "box1")
N=driver.find_element(By.ID, "box101")

Stockholm_ele=driver.find_element(By.ID, "box2")
swedan=driver.find_element(By.ID, "box102")


act.drag_and_drop(rome_ele,italy_ele).perform() # drag and drop opration
act.drag_and_drop(Stockholm_ele,swedan).perform()
act.drag_and_drop(Oslo_ele,N).perform()
act.drag_and_drop(Madrid_ele,spain).perform()
act.drag_and_drop(Washington_ele,U).perform()
act.drag_and_drop(Seoul_ele,south).perform()
act.drag_and_drop(Copenhagen_ele,norway).perform()

