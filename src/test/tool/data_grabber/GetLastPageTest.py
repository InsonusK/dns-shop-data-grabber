import unittest
from src.main.tool.data_grabber.GetLastPage import get_last_page
from src.main.tool.DriverFactory import DriverFactory


class GetLastPageTest(unittest.TestCase):
    def test_get_correct_last_page(self):
        print("test depends on site")
        url = "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/"
        page_reader = DriverFactory("/home/insonusk/Documents/chromedriver_linux64/chromedriver")
        result = page_reader.parse(url, get_last_page)
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()
