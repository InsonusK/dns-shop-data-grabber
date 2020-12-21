import unittest
from src.main.tool.data_grabber.GetLinksFromCardList import get_links_price_from_card_list
from src.main.tool.DriverFactory import DriverFactory

class GetLastPageTest(unittest.TestCase):
    def test_get_amount_of_links(self):
        print("test depends on site")
        url = "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/"
        page_reader = DriverFactory("/home/insonusk/Documents/chromedriver_linux64/chromedriver")
        result = page_reader.parse(url, get_links_price_from_card_list)
        self.assertEqual(len(result), 18)


if __name__ == '__main__':
    unittest.main()