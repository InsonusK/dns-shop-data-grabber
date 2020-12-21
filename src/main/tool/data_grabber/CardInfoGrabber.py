import re
from src.main.tool.CardInfo import CardInfo
from src.main.tool.DriverFactory import DriverFactory
from src.main.tool.parser.PriceParser import PriceParser
from src.main.tool.parser.WattParser import watt_parser
from src.main.tool.DriverFactory import DriverFactory, CSS_Search_Element
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException

class CardInfoGrabber:
    def __init__(self, driver_factory: DriverFactory):
        self.driver_factory = driver_factory

    def get_from_url(self, url: str) -> CardInfo:
        card_info = CardInfo(url)
        parUrl = url + "characteristics/"

        print(f'--- Grab url {parUrl}')
        driver = self.driver_factory.getDriver(parUrl)
        self.__grab_from_driver__(driver, card_info)
        driver.quit()

        return card_info

    def __grab_from_driver__(self, driver: WebDriver, card_info: CardInfo) -> CardInfo:
        try:
            card_info.name = CSS_Search_Element(driver, ".product-card-tabs__product-title").text
        except TimeoutException as e:
            print(e)

        try:
            card_info.price = PriceParser(CSS_Search_Element(driver, ".product-card-price__current").text)
        except TimeoutException as e:
            print(e)

        try:
            characteristics_table = CSS_Search_Element(driver, ".product-characteristics")
            characteristics_rows = characteristics_table.find_elements_by_css_selector("tr")

            max_wat_pattern = re.compile("Максимальное энергопотребление")
            for characteristic in characteristics_rows:
                cols = characteristic.find_elements_by_css_selector("td")
                if len(cols) > 2:
                    raise Error("Wrong amount of characteristic columns while parsing")

                if cols[0].text == "Год релиза":
                    card_info.release = int(cols[1].text)
                if cols[0].text == "Рекомендуемый блок питания":
                    card_info.offer_charge_block = watt_parser(cols[1].text)
                if max_wat_pattern.match(cols[0].text):
                    card_info.max_watt = watt_parser(cols[1].text)
        except TimeoutException as e:
            print(e)

        return card_info
