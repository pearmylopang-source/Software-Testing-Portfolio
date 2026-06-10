from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_page(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)

    username_field = wait.until(
        EC.presence_of_element_located((By.NAME, "user-name"))
    )
    username_field.send_keys("standard_user")

    password_field = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    wait.until(EC.url_contains("inventory"))

    print("Login test passed! Redirected to:", driver.current_url)

driver = webdriver.Chrome()
test_login_page(driver)
driver.quit()