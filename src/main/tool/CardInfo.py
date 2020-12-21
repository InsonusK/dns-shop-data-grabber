import datetime




class CardInfo:
    name: str
    price: (int, str)
    release: int
    max_watt: int
    offer_charge_block: int
    url: str

    def __init__(self, url: str):
        self.url = url
