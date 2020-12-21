def PriceParser(price: str) -> (int, str):
    priceCond = price.replace(" ", "")
    for i in range(len(priceCond)):
        if not priceCond[i].isnumeric():
            return (int(priceCond[:i]), priceCond[i:])
    raise Error(f'wrong price : {price}')



