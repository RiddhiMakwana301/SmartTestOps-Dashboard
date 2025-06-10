from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ajax_loaded_content():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")
    
    # Click start button
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    
    # Wait for the dynamic text to appear (more specific XPath)
    hello_world_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='finish']/h4[text()='Hello World!']")
        )
    )
    
    # Assert the exact text
    assert hello_world_element.text == "Hello World!"
    driver.quit()