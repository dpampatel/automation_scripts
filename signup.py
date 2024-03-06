from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

try:
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Set up the Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    # Load the Udemy sign-up page
    driver.get("https://www.u--demy.com/join/signup-popup/")

    # Wait for the page to load
    time.sleep(5)

    # Find full name, email, password, and checkbox fields and enter information
    full_name_field = driver.find_element(By.ID, "form-group--1")
    full_name_field.send_keys("Your Full Name")

    email_field = driver.find_element(By.ID, "form-group--3")
    email_field.send_keys("your_email@example.com")

    password_field = driver.find_element(By.ID, "form-group--5")
    password_field.send_keys("your_password")

    checkbox = driver.find_element(By.ID, "checkbox--7")
    # checkbox.click()
    # driver.execute_script("arguments[0].checked = true;", checkbox)
    checkbox.send_keys(Keys.SPACE)


    # Find and click the sign-up button
    sign_up_button = driver.find_element(By.XPATH, "//button[.//span[text()='Sign up']]")
    # sign_up_button.click()

    # Wait for the sign-up process to complete
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)
    # Close the browser
    driver.quit()
