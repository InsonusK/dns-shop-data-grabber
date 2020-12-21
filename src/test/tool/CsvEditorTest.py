import unittest
from src.main.tool.CsvEditor import CsvEditor
from src.main.tool.CardInfo import CardInfo
import os


class CsvEditorTest(unittest.TestCase):
    def test_add(self):
        try:
            os.remove("test1.csv")
        except FileNotFoundError:
            print("first run")
        editor = CsvEditor("test1")
        info = CardInfo("url1")
        info.name = "n"
        info.price = 1
        info.offer_charge_block = 2
        info.release = 3
        info.max_watt = 4

        editor.add_card_to_csv(info)

    def test_search(self):
        try:
            os.remove("test2.csv")
        except FileNotFoundError:
            print("first run")
        editor = CsvEditor("test2")
        info = CardInfo("url1")
        info.name = "n"
        info.price = (1, "c")
        info.offer_charge_block = 2
        info.release = 3
        info.max_watt = 4

        editor.add_card_to_csv(info)
        search_res = editor.find_url_in_file("url1")
        self.assertTrue(search_res[0])
        self.assertEquals(search_res[1][0], 1)
        self.assertEquals(search_res[1][1], "c")

    def test_change(self):
        try:
            os.remove("test3.csv")
        except FileNotFoundError:
            print("first run")
        editor = CsvEditor("test3")
        info = CardInfo("url1")
        info.name = "n"
        info.price = (1, "c")
        info.offer_charge_block = 2
        info.release = 3
        info.max_watt = 4

        editor.add_card_to_csv(info)
        search_res = editor.change_card_price("url1", (2,"b"))
        search_res = editor.find_url_in_file("url1")
        self.assertTrue(search_res[0])
        self.assertEquals(search_res[1][0], 2)
        self.assertEquals(search_res[1][1], "2")

if __name__ == '__main__':
    unittest.main()