import unittest
from src.main.tool.parser.TotalCountTextParser import total_count_text_parser


class TotalCountTextParserTest(unittest.TestCase):
    def test_space_before_stock_word_is_correct(self):
        self.assertEqual(total_count_text_parser("123 321 Товаров"), 123321)

    def test_no_space_before_stock_word_is_correct(self):
        self.assertEqual(total_count_text_parser("123 321Товаров"), 123321)

    def test_no_stock_word_is_correct(self):
        self.assertEqual(total_count_text_parser("123 321"), 123321)

if __name__ == '__main__':
    unittest.main()
