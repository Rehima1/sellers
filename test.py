from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Step 1: Set up Chrome options (run in headless mode if you don't want the browser UI)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Optional: Headless mode if you don't want to see the browser
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Step 2: Specify the path to chromedriver
chrome_driver_path = r'C:\path\to\chromedriver.exe'  # Replace with your actual chromedriver path
service = Service(chrome_driver_path)

# Step 3: Launch the Chrome browser
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 4: Navigate to Google
driver.get("https://www.google.co.uk/")

# Step 5: Locate the search box and submit a query
search_box = driver.find_element(By.NAME, "q")  # 'q' is the name of the search box in Google's HTML
search_box.send_keys("Selenium WebDriver tutorial")  # Enter the search term
search_box.submit()  # Submit the search

# Step 6: Wait for results to load (optional)
time.sleep(3)

# Step 7: Close the browser
driver.quit()

