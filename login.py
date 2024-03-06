from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

try:
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Set up the Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    # Load the Udemy website
    driver.get("https://www.u--demy.com/join/login-popup/")
    # Wait for the page to load
    time.sleep(5)

    # Find email and password fields and enter credentials
    email_field = driver.find_element(By.ID, "form-group--1")
    email_field.send_keys("deepampatel14@yahoo.com")

    password_field = driver.find_element(By.ID, "form-group--3")
    password_field.send_keys("ABCDEFGH")

    # Find and click the login button
    login_button = driver.find_element(By.XPATH, "//button[.//span[text()='Log in']]")
    login_button.click()

    # Wait for the login process to complete
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)
    # Close the browser
    driver.quit()
