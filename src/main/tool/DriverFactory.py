from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class DriverFactory:

    def __init__(self, chromedriver_path: str):
        self.__chromedriver_path = chromedriver_path

    def getDriver(self, url) -> WebDriver:
        driver = webdriver.Chrome(executable_path=self.__chromedriver_path)
        driver.get(url)
        return driver

    def parse(self, url, parse_logic):
        driver = self.getDriver(url)
        data = parse_logic(driver)
        driver.quit()
        return data


def CSS_Search_Element(driver: WebDriver, css: str) -> WebElement:
    try:
        return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    except TimeoutException:
        raise

def CSS_Search_Elements(driver: WebDriver, css: str) -> WebElement:
    try:
        return WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))
    except TimeoutException:
        raise



