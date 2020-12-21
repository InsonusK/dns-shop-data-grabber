from selenium.webdriver.chrome.webdriver import WebDriver
from src.main.tool.data_grabber.GetLastPage import get_last_page
from src.main.tool.data_grabber.GetTotalCards import get_total_cards


class BaseData:
    total_pages: int
    total_cards: int


def get_base_data(driver: WebDriver) -> BaseData:
    base_data = BaseData()
    base_data.total_pages = get_last_page(driver)
    base_data.total_cards = get_total_cards(driver)
    return base_data
