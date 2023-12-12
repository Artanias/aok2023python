from collections import defaultdict


CARDS = "23456789TJQKA"
CNT_CARDS = len(CARDS)
CNT_CARDS_IN_HAND = 5


def get_cnt_letters(hand: str) -> dict[str, int]:
    letters_cnt = defaultdict(lambda: 0)
    for letter in hand:
        letters_cnt[letter] += 1
    return letters_cnt


def calc(lines: list[str]) -> int:
    hands_scores = []
    for line in lines:
        hand, bid_amount = line.split()
        bid_amount = int(bid_amount)
        line_score = sum(
            (CARDS.find(letter) * CNT_CARDS**i) for i, letter in enumerate(hand[::-1])
        )
        cnt_letters = get_cnt_letters(hand)
        cnt_uniq = len(cnt_letters)
        # five of a kind
        if cnt_uniq == 1:
            line_score += CNT_CARDS ** (CNT_CARDS_IN_HAND + 6)
        elif cnt_uniq == 2:
            # four of a kind
            if cnt_letters[next(iter(cnt_letters.keys()))] in (1, 4):
                line_score += CNT_CARDS ** (CNT_CARDS_IN_HAND + 5)
            # full house
            else:
                line_score += CNT_CARDS ** (CNT_CARDS_IN_HAND + 4)
        elif cnt_uniq == 3:
            # three of a kind
            if any(cnt == 3 for cnt in cnt_letters.values()):
                line_score += CNT_CARDS ** (CNT_CARDS_IN_HAND + 3)
            # two pair
            else:
                line_score += CNT_CARDS ** (CNT_CARDS_IN_HAND + 2)
        # one pair
        elif cnt_uniq == 4:
            line_score += CNT_CARDS ** (CNT_CARDS_IN_HAND + 1)
        hands_scores.append((hand, bid_amount, line_score))
    hands_scores.sort(key=lambda el: el[2])
    return sum(rank * hand[1] for rank, hand in enumerate(hands_scores, start=1))
