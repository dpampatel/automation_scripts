from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Set up the Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    # Load the Udemy sign-up page
    driver.get("https://b--usiness.udemy.com/request-demo-mx/?utm_source=direct&utm_medium=direct")

    # Wait for the page to load
    time.sleep(5)

    # Find fields and enter information
    driver.find_element(By.ID, "FirstName").send_keys("D")
    driver.find_element(By.ID, "LastName").send_keys("P")
    driver.find_element(By.ID, "Email").send_keys("d.p@example.com")
    driver.find_element(By.ID, "Phone").send_keys("1234567890")

    # Select "CA" from the country dropdown
    driver.execute_script("var select = document.getElementById('Person_Country__c'); var option = document.createElement('option'); option.text = 'Canada'; option.value = 'CA'; select.appendChild(option);")
    country_dropdown = driver.find_element(By.ID, "Person_Country__c").send_keys("Canada")

    # Enter company name
    driver.find_element(By.ID, "Company").send_keys("DP Corp")

    # Select "1-199" from the employee tier dropdown
    driver.find_element(By.ID, "Employee_Tier__c").send_keys("1-199")

    # Select "21 - 200" from the initial seat count dropdown
    driver.find_element(By.ID, "Initial_Seat_Count__c").send_keys("21 - 200")

    # Enter job title
    driver.find_element(By.ID, "Title").send_keys("Manager")

    # Enter job level
    driver.find_element(By.ID, "jobLevelfromLead").send_keys("Manager")

    # Enter organization's training needs
    driver.find_element(By.ID, "UFO_Comments__c").send_keys("We need training in various fields.")

    # Find and click the submit button using class name
    # submit_button = driver.find_element(By.CLASS_NAME, "mktoButton")
    # submit_button.click()

    submit_button_xpath = "//button[contains(., 'Submit')]"
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))

    # Move the mouse cursor to the submit button
    ActionChains(driver).move_to_element(submit_button).perform()

    # Click the submit button
    submit_button.click()
    # Wait for the submission process to complete
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(20)
    # Close the browser
    driver.quit()
