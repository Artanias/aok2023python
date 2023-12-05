import re
from typing import Iterable
from pathlib import Path


EXAMPLE_PATH = Path("example.txt")
EXAMPLE2_PATH = Path("example2.txt")
DATA_PATH = Path("data.txt")
NUM_PATTERN = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|\d)")
LAST_NUM_PATTERN = re.compile(fr"(?s:.*){NUM_PATTERN.pattern}")


def get_lines(path: Path) -> list[str]:
    return path.read_text().splitlines()


def convert_str_to_int(num: str) -> int:
    match num:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9
        case _:
            return int(num)


def get_next_calibration_value(path: Path) -> Iterable[int]:
    for line in get_lines(path):
        first_num = re.search(NUM_PATTERN, line).group()
        last_num = re.search(LAST_NUM_PATTERN, line).group(1)
        num = int(
            f"{convert_str_to_int(first_num)}{convert_str_to_int(last_num)}"
        )
        yield num


if __name__ == '__main__':
    for path in [EXAMPLE_PATH, EXAMPLE2_PATH, DATA_PATH]:
        result = sum(get_next_calibration_value(path))
        print(result)
