def test_add_to_cart(driver):
    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Add item to cart
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    cart_badge = driver.find_element("class name", "shopping_cart_badge")
    
    assert cart_badge.text == "1"
