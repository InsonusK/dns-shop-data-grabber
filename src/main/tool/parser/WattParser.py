def watt_parser(watt: str) -> int:
    wattCond = watt.replace(" ", "")
    for i in range(len(wattCond)):
        if not wattCond[i].isnumeric():
            return int(wattCond[:i])
    return int(wattCond)
