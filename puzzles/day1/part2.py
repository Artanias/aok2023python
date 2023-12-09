import re
from typing import Iterable


NUM_PATTERN = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|\d)")
LAST_NUM_PATTERN = re.compile(rf"(?s:.*){NUM_PATTERN.pattern}")


def convert_str_to_int(num: str) -> int:
    match num:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return int(num)


def get_next_calibration_value(lines: list[str]) -> Iterable[int]:
    for line in lines:
        first_num = re.search(NUM_PATTERN, line).group()
        last_num = re.search(LAST_NUM_PATTERN, line).group(1)
        num = int(f"{convert_str_to_int(first_num)}{convert_str_to_int(last_num)}")
        yield num


def calc(lines: list[str]) -> int:
    result = sum(get_next_calibration_value(lines))
    return result
