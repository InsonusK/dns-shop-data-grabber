import unittest
from src.main.tool.data_grabber.CardInfoGrabber import CardInfoGrabber
from src.main.tool.DriverFactory import DriverFactory
from src.main.tool.CardInfo import CardInfo


class GradCardInfoTest(unittest.TestCase):

    def test1(self):
        print("This test is depends on data from site")
        print("This test is depends on path to chromedriver")
        url = "https://www.dns-shop.ru/product/51b2d9e911261b80/videokarta-evga-geforce-rtx-3090-xc3-ultra-gaming-24g-p5-3973-kr/"
        driver_factory = DriverFactory("/home/insonusk/Documents/chromedriver_linux64/chromedriver")
        grabber = CardInfoGrabber(driver_factory)
        cardInfo: CardInfo = grabber.get_from_url(url)
        self.assertEqual(cardInfo.name, "Видеокарта EVGA GeForce RTX 3090 XC3 ULTRA GAMING [24G-P5-3973-KR]")
        self.assertEqual(cardInfo.price, (174999,"₽"))
        self.assertEqual(cardInfo.release, 2020)
        self.assertEqual(cardInfo.max_watt, 350)
        self.assertEqual(cardInfo.offer_charge_block, 750)
        self.assertEqual(cardInfo.url, url)

    def test2(self):
        print("This test is depends on data from site")
        print("This test is depends on path to chromedriver")
        url = "https://www.dns-shop.ru/product/4e2d2341ce283330/videokarta-msi-geforce-gt-710-silent-lp-gt-710-1gd3h-lp/"
        driver_factory = DriverFactory("/home/insonusk/Documents/chromedriver_linux64/chromedriver")
        grabber = CardInfoGrabber(driver_factory)
        cardInfo: CardInfo = grabber.get_from_url(url)
        self.assertEqual(cardInfo.name, "Видеокарта MSI GeForce GT 710 Silent LP [GT 710 1GD3H LP]")
        self.assertEqual(cardInfo.price, (2850,"₽"))
        self.assertEqual(cardInfo.release, 2014)
        self.assertEqual(cardInfo.max_watt, 19)
        self.assertEqual(cardInfo.offer_charge_block, 300)
        self.assertEqual(cardInfo.url, url)

if __name__ == '__main__':
    unittest.main()
