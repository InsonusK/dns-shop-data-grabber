import unittest
from src.main.tool.data_grabber.GetBaseData import get_base_data, BaseData
from src.main.tool.DriverFactory import DriverFactory


class GetBaseDataTest(unittest.TestCase):
    def test_BaseData(self):
        print("Test depends of site")
        url = "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/"
        page_reader = DriverFactory("/home/insonusk/Documents/chromedriver_linux64/chromedriver")
        baseDt: BaseData = page_reader.parse(url, get_base_data)
        self.assertEqual(baseDt.total_cards, 252)
        self.assertEqual(baseDt.total_pages, 14)


if __name__ == '__main__':
    unittest.main()
