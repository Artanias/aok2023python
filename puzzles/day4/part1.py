def calc(lines: list[str]) -> int:
    result = 0
    for line in lines:
        _, numbers = line.split(":")
        won_nums, my_nums = numbers.split("|")
        won_nums = [int(num) for num in won_nums.split()]
        my_nums = [int(num) for num in my_nums.split()]
        my_won_cards_cnt = len([num for num in my_nums if num in won_nums])
        if not my_won_cards_cnt:
            continue
        card_worth = 2 ** (my_won_cards_cnt - 1)
        result += card_worth
    return result
