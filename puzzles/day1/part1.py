import re
from typing import Iterable


def get_next_calibration_value(lines: list[str]) -> Iterable[int]:
    for line in lines:
        all_numbers = re.findall("\d", line)
        yield int(f"{all_numbers[0]}{all_numbers[-1]}")


def calc(lines: list[str]) -> int:
    result = sum(get_next_calibration_value(lines))
    return result
