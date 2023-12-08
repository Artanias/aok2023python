def set_won_cnt(
    card_num: int, numbers: str, cnt_cards: int, card_won_cnt: dict[int, int]
) -> int:
    won_nums, my_nums = numbers.split("|")
    won_nums = [int(num) for num in won_nums.split()]
    my_won_cards_cnt = len([num for num in my_nums.split() if int(num) in won_nums])
    if card_num + my_won_cards_cnt > cnt_cards:
        card_won_cnt[card_num] = cnt_cards - card_num
    else:
        card_won_cnt[card_num] = my_won_cards_cnt
    return my_won_cards_cnt


def calc(lines: list[str]) -> int:
    card_won_cnt = {}
    cnt_cards = len(lines)
    for line in lines:
        card_info, numbers = line.split(":")
        card_num = int(card_info.split()[-1])
        set_won_cnt(card_num, numbers, cnt_cards, card_won_cnt)
    card_score = {card_num: 1 for card_num in card_won_cnt}
    for card_num, value in card_won_cnt.items():
        for i in range(card_num + 1, card_num + value + 1):
            card_score[i] += card_score[card_num]
    return sum(num for num in card_score.values())
