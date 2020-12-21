from src.main.tool.data_grabber.CardCatalogGrabber import CardCatalogGrabber
from src.main.tool.CardInfo import CardInfo
from src.main.tool.CsvEditor import CsvEditor
from datetime import datetime
from src.main.tool.DriverFactory import DriverFactory


def GrabCardsFromDns():
    chromedriver_path = "/home/insonusk/Documents/chromedriver_linux64/chromedriver"
    url = "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/"
    driver_f = DriverFactory(chromedriver_path)
    csv_e = CsvEditor(f'DnsList')
    catalag_g = CardCatalogGrabber(csv_e, driver_f)
    catalag_g.grab_url(url)
