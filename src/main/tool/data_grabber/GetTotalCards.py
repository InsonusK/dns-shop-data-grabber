from selenium.webdriver.chrome.webdriver import WebDriver
from src.main.tool.parser.TotalCountTextParser import total_count_text_parser
from src.main.tool.DriverFactory import CSS_Search_Element


def get_total_cards(driver: WebDriver) -> int:
    total_count_text = CSS_Search_Element(driver, ".products-count")
    return total_count_text_parser(total_count_text.text)
