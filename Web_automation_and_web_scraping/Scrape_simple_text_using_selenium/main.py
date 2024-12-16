from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
    driver.get("https://automated.pythonanywhere.com")
    return driver


def clear_text(text):
    """This function return average temperature from text"""
    temperature = float(text.split(": ")[1])
    return temperature


def main():
    driver = get_driver()
    time.sleep(3)
    dynamic_element = driver.find_element(By.XPATH, "//*[@class='text-success']")
    return clear_text(dynamic_element.text)


print(main())