from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Set up the Firefox options
options = Options()
options.set_preference("profile", "/home/sillah/snap/firefox/common/.mozilla/firefox/v7kd3avn.sillah")  # Change this to the correct path

# Set up the Firefox service
service = Service('/usr/local/bin/geckodriver')  # Change this to the path of your geckodriver

# Start the Firefox driver with the specified options and service
driver = webdriver.Firefox(service=service)

# Load the local HTML file
driver.get("https://www.upwork.com/freelance-jobs/artificial-intelligence/")
driver.implicitly_wait(10) 
# Find the "Load more jobs" button by its class name
load_more_button = driver.find_element(By.CSS_SELECTOR, "a[data-qa='load-more']")

# Click the button
load_more_button.click()

# Optionally, wait for some time to observe the result
import time
time.sleep(10)
# Perform actions with the driver
job_elements = driver.find_elements(By.CSS_SELECTOR, "[data-qa='job-tile']")
for job_element in job_elements:
    job_title_element = job_element.find_element(By.CSS_SELECTOR, "[data-qa='job-title']")
    print(job_title_element)
    job_title = job_title_element.text
    job_link = job_title_element.get_attribute("href")
    price_element = job_element.find_element(By.CSS_SELECTOR, ".text-muted-on-inverse")
    price = price_element.text

    # Extract price
    posted_on_element = job_element.find_element(By.CSS_SELECTOR, ".text-muted-on-inverse + small")
    posted_date = posted_on_element.text
    print(f"Job element: {job_elements}")
    print(f"Job Title: {job_title}")
    print(f"Job Link: {job_link}")
    print(f"Posted Date: {posted_date}")
    print(f"Price: {price}")
    print("-" * 40)


# # Quit the driver
# driver.quit()
