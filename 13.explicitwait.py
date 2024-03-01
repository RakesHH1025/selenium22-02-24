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
    driver.get("https://www.example.com")
    element = driver.find_element(By.ID, "nonexistent_element_id")

    # If the element is found, this won't execute
    print("Element found")

except NoSuchElementException:
    # Handle the NoSuchElementException exception
    print("Element not found")

finally:
    # Close the browser window
    driver.quit()
