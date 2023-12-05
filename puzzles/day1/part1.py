import re
from typing import Iterable
from pathlib import Path


EXAMPLE_PATH = Path("example.txt")
DATA_PATH = Path("data.txt")


def get_lines(path: Path) -> list[str]:
    return path.read_text().splitlines()


def get_next_calibration_value(path: Path) -> Iterable[int]:
    for line in get_lines(path):
        all_numbers = re.findall("\d", line)
        yield int(f"{all_numbers[0]}{all_numbers[-1]}")


for path in [EXAMPLE_PATH, DATA_PATH]:
    result = sum(get_next_calibration_value(path))
    print(result)
