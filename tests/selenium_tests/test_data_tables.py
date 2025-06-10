from selenium import webdriver
from selenium.webdriver.common.by import By

def test_table_sorting():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    
    # Click age column header to sort
    driver.find_element(By.XPATH, "//div[text()='Age']").click()
    
    # Get all age values from the table
    ages = driver.find_elements(By.CSS_SELECTOR, ".rt-td:nth-child(3)")
    age_values = [int(age.text) for age in ages if age.text.isdigit()]
    
    # Verify sorted order
    assert age_values == sorted(age_values), "Ages are not sorted!"
    driver.quit()