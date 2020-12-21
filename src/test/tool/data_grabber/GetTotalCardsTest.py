import unittest
from src.main.tool.data_grabber.GetTotalCards import get_total_cards
from src.main.tool.DriverFactory import DriverFactory

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("test depends on site")
        url = "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/"
        page_reader = DriverFactory("/home/insonusk/Documents/chromedriver_linux64/chromedriver")
        result = page_reader.parse(url, get_total_cards)
        self.assertEqual(252,result)


if __name__ == '__main__':
    unittest.main()
