import contextlib
from typing import NamedTuple


class NumNeighbor(NamedTuple):
    number: int
    stars: list[tuple[int, int]]


def calc_gear_ratio(
    numbers: list[NumNeighbor], stars: list[tuple[int, int]], number: int
) -> int:
    result = 0
    for number_val in numbers:
        for star in number_val.stars:
            if star in stars:
                result += number * number_val.number
    return result


def calc(lines: list[str]) -> int:
    numbers: list[NumNeighbor] = []
    result = 0
    for i, line in enumerate(lines):
        next_num = ""
        stars = []
        for j, letter in enumerate(line):
            if letter.isdigit():
                next_num = f"{next_num}{letter}"
                for k, g in [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j + 1),
                    (i + 1, j),
                ]:
                    with contextlib.suppress(IndexError):
                        if lines[k][g] == "*" and (k, g) not in stars:
                            stars.append((k, g))
            elif next_num:
                int_num = int(next_num)
                result += calc_gear_ratio(numbers, stars, int_num)
                numbers.append(NumNeighbor(int_num, stars))
                next_num = ""
                stars = []
        if next_num:
            int_num = int(next_num)
            result += calc_gear_ratio(numbers, stars, int_num)
            numbers.append(NumNeighbor(int_num, stars))
    return result
