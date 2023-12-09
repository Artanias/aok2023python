from functools import reduce


def calc(lines: list[str]) -> int:
    result = 0
    for line in lines:
        _, subsets = line.split(":")
        max_color = {"red": 0, "green": 0, "blue": 0}
        for subset in subsets.split(";"):
            for cube in subset.split(","):
                cnt, color = cube.strip().split(maxsplit=1)
                color = color.strip()
                cnt = int(cnt)
                if cnt > max_color[color]:
                    max_color[color] = cnt
        result += reduce(lambda x, y: x * max_color[y], max_color, 1)
    return result
