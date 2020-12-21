import unittest
from src.main.tool.parser.PriceParser import PriceParser

class PriceParserTest(unittest.TestCase):
    def test_space_before_currency_is_correct(self):
        self.assertEqual(PriceParser("123 321 ₽"), (123321, '₽'))

    def test_no_space_before_currency_is_correct(self):
        self.assertEqual(PriceParser("123 321₽"), (123321, '₽'))

if __name__ == '__main__':
    unittest.main()