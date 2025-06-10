from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")

    # Wait for page to load completely
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    # Scroll to the form (helps with element visibility)
    driver.execute_script("window.scrollBy(0, 200)")

    # Fill required fields
    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("john@example.com")

    # Gender selection - More reliable approach
    male_radio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']"))
    )
    driver.execute_script("arguments[0].click();", male_radio)

    # Mobile number (required field)
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")

    # Submit form
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    driver.execute_script("arguments[0].click();", submit_button)

    # Validation
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        success_text = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
        assert "Thanks for submitting the form" in success_text
    finally:
        driver.quit()