from selenium import webdriver
from selenium.webdriver.common.by import By
from Web_automation_and_web_scraping.constant_variables import *
from datetime import datetime
import time


def generate_file_with_current_temperature(current_temperature):
    file_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.txt'
    with open(file_name, 'w') as f:
        f.write(f"{current_temperature}")


def clear_text(text: str) -> float:
    return float(text.split(": ")[1])


def get_driver():
    # Set option that making browsing easier
    options = webdriver.ChromeOptions()

    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sand-box")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomatedControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(LOGIN_URL)
    return driver


def main():
    driver = get_driver()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys(USER_NAME)
    driver.find_element(By.XPATH, "//*[@id='id_password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    driver.find_element(By.XPATH, "//*[@class='navbar-brand']").click()
    while True:
        time.sleep(2)
        dynamic_element = driver.find_element(By.XPATH, "//*[@class='text-success']")
        current_temperature = clear_text(dynamic_element.text)
        generate_file_with_current_temperature(current_temperature)


main()
