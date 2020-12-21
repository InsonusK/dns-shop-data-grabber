from src.main.tool.CardInfo import CardInfo
import csv

def GetUrlColName() -> str:
    return "Url"

def GetPriceColName() -> str:
    return "Price"

def GetCurrencyColName() -> str:
    return "Currency"

def GetCardInfoCsvHead() -> [str]:
    return ["Name", GetPriceColName(), GetCurrencyColName(), "Release", "Max_Watt", "Offered charge power", GetUrlColName()]


def CardToStringArr(card: CardInfo) -> [str]:
    return [card.name, card.price[0], card.price[1], card.release, card.max_watt, card.offer_charge_block, card.url]


class CsvEditor:
    def __init__(self, fileName: str):
        self.fileName = fileName
        with open(f'{self.fileName}.csv', mode='w') as card_file:
            card_writer = self.__writer_builder__(card_file)
            card_writer.writerow(GetCardInfoCsvHead())
            card_file.close()


    def find_url_in_file(self, url: str) -> (bool, (int, str)):
        with open(f'{self.fileName}.csv', mode='r') as card_file:
            card_search = csv.reader(card_file, delimiter=';')
            url_col = -1
            price_col = -1
            cur_col = -1
            for line_index,row  in enumerate(card_search):
                if line_index == 0:
                    for index, col in enumerate(row):
                        if col == GetUrlColName():
                            url_col = index
                        if col == GetPriceColName():
                            price_col = index
                        if col == GetCurrencyColName():
                            cur_col = index
                else:
                    if row[url_col] == url:
                        return (True, (int(row[price_col]), row[cur_col]))
            card_file.close()
        return (False, (0,""))

    def add_card_to_csv(self, card: CardInfo):
        with open(f'{self.fileName}.csv', mode='a') as card_file:
            card_writer = self.__writer_builder__(card_file)
            card_writer.writerow(CardToStringArr(card))
            card_file.close()

    def add_cards_to_csv(self, card_arr: [CardInfo]):
        with open(f'{self.fileName}.csv', mode='a') as card_file:
            card_writer = self.__writer_builder__(card_file)
            for card in card_arr:
                card_writer.writerow(CardToStringArr(card))
            card_file.close()

    def change_card_price(self, url: str, price: (int,str)):
        ##you could use pandas
        with open(f'{self.fileName}.csv', mode='w') as card_file:
            card_writer = self.__writer_builder__(card_file)
            url_col = -1
            price_col = -1
            cur_col = -1
            for line_index, row in enumerate(card_writer):
                if line_index == 0:
                    for index, col in enumerate(row):
                        if col == GetUrlColName():
                            url_col = index
                        if col == GetPriceColName():
                            price_col = index
                        if col == GetCurrencyColName():
                            cur_col = index
                else:
                    if row[url_col] == url:
                        row[price_col] = price[0]
                        row[cur_col] = price[1]
            card_file.close()

    def __writer_builder__(self, card_file):
        return csv.writer(card_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
