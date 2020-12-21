from src.main.tool.data_grabber.GetLinksFromCardList import get_links_price_from_card_list
from src.main.tool.data_grabber.CardInfoGrabber import CardInfoGrabber
from src.main.tool.CardInfo import CardInfo
from src.main.tool.CsvEditor import CsvEditor
from src.main.tool.DriverFactory import DriverFactory


class CardFromListGrabber:
    def __init__(self, csv_editor: CsvEditor, driver_factory: DriverFactory):
        self.csvEditor = csv_editor
        self.driver_factory = driver_factory

    def grab_url(self, url: str):
        print(f'-- get links from url {url}')
        links: [(str, (int, str))] = self.driver_factory.parse(url, get_links_price_from_card_list)
        print(f'-- found {len(links)} links')

        card_info_arr: [] = []
        card_info_grabber = CardInfoGrabber(self.driver_factory)
        for link in links:
            print(f'-- link: {link}')
            search_res = self.csvEditor.find_url_in_file(url):
            if not search_res[0]:
                card_info = card_info_grabber.get_from_url(link)
                card_info_arr.append(card_info)
            else if link[1][0] != search_res[1][0] || link[1][1] != search_res[1][1]

        if len(card_info_arr) > 0:
            self.csvEditor.add_cards_to_csv(card_info_arr)
        return card_info_arr

