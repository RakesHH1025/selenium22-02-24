from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Initialize the WebDriver

S=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
O=webdriver.ChromeOptions()
O.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=O, service=S)


try:
    # Attempt to find an element that doesn't exist
    driver.get("https://wwwsaaas.google.com/")

    driver.maximize_window()

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("Selenium")
    search_box.submit()

    # If the element is found, this won't execute
    print("Element found")

except:
    # Handle the NoSuchElementException exception
    print("Element not found")

finally:
    # Close the browser window
    driver.quit()
