from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
# driver = webdriver.Chrome()
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv=Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options, service=serv)

# Maximize the window
driver.maximize_window()

# Open Amazon website
driver.get("https://www.amazon.com/")

# Find the search box and input 'mobile phones'
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("mobile phones")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "s-result-item"))
    )
except Exception as e:
    print("An error occurred while waiting for search results:", e)

# Filter the search results by price range
min_price = 200  # Minimum price
max_price = 500  # Maximum price

# Constructing XPath for price filter
price_filter_xpath = f"//span[@class='a-price-whole'][not(contains(text(), '{min_price - 1}')) and not(contains(text(), '{max_price + 1}'))]"

# Click on the 'Price' filter dropdown
price_filter_dropdown = driver.find_element(By.XPATH, "//span[text()='Price']/ancestor::a")
price_filter_dropdown.click()

# Select '200 to 500' from the dropdown
price_range_option = driver.find_element(By.XPATH, "//a[contains(text(),'Under $500')]")
price_range_option.click()

# Wait for the page to update with the filtered results
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, price_filter_xpath))
    )
except Exception as e:
    print("An error occurred while waiting for filtered results:", e)

# Selecting the first mobile phone within the specified price range
mobile_phone = driver.find_element(By.XPATH, price_filter_xpath + "/ancestor::div[@class='s-result-item']//a")
mobile_phone.click()

# Wait for the mobile phone page to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    )
except Exception as e:
    print("An error occurred while waiting for mobile phone page to load:", e)

# Print the title of the selected mobile phone
mobile_phone_title = driver.find_element(By.ID, "productTitle").text
print("Selected Mobile Phone:", mobile_phone_title)

# Close the browser
driver.quit()
