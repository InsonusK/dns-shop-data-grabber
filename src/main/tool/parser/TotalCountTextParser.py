def total_count_text_parser(total_count_text: str) -> int:
    cond = total_count_text.replace(" ", "")
    for i in range(len(cond)):
        if not cond[i].isnumeric():
            return int(cond[:i])
    return int(cond)
    raise Error(f'wrong total count text: {total_count_text}')