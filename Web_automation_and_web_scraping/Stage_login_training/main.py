from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep as sl
from Web_automation_and_web_scraping.constant_variables import *


def get_driver():
    # Set option that making browsing easier
    options = webdriver.ChromeOptions()

    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sand-box")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomatedControlled")
    options.add_experimental_option("prefs", {
                                                        "credentials_enable_service": False,
                                                        "profile.password_manager_enabled": False
                                                        })

    driver = webdriver.Chrome(options=options)
    driver.get(HOME_PAGE_URL)
    return driver


def main():
    expected_url = "https://chayowfaxy.stage.ntgdev.com/page/privacy"
    driver = get_driver()
    waiter = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    waiter.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-tid='header-login-btn']")))
    driver.find_element(By.XPATH, "//*[@data-tid='header-login-btn']").click()
    waiter.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-tid='login-email-input']")))
    driver.find_element(By.XPATH, "//*[@data-tid='login-email-input']").send_keys(STAGE_LOGIN)
    driver.find_element(By.XPATH, "//*[@data-tid='login-password-input']").send_keys(STAGE_PASSWORD)
    driver.find_element(By.XPATH, "//*[@data-tid='login-btn']").click()
    sl(10)
    waiter.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-tid='close-modal']"))).click()
    privacy_policy_element = driver.find_element(By.XPATH, "//*[@data-tid='footer-terms-2']")
    action.move_to_element(privacy_policy_element).perform()
    privacy_policy_element.click()
    if driver.current_url == expected_url:
        return True
    else:
        return False


print(main())

