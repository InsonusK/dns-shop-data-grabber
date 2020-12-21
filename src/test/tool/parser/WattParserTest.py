import unittest
from src.main.tool.parser.WattParser import watt_parser


class WattParserTest(unittest.TestCase):
    def test_space_before_watt_is_correct(self):
        self.assertEqual(watt_parser("123 321 Вт"), 123321)

    def test_no_space_before_currency_is_correct(self):
        self.assertEqual(watt_parser("123 321Вт"), 123321)

    def test_no_watt_is_correct(self):
        self.assertEqual(watt_parser("123 321"), 123321)

if __name__ == '__main__':
    unittest.main()