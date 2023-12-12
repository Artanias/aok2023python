def calc(lines: list[str]) -> int:
    result = 0
    for line in lines:
        numbers = [list(map(int, line.split()))]
        levels = 0
        while any(num != 0 for num in numbers[levels]):
            numbers.append(
                [
                    numbers[levels][i + 1] - numbers[levels][i]
                    for i in range(len(numbers[levels]) - 1)
                ]
            )
            levels += 1
        for i in range(levels, 0, -1):
            numbers[i - 1].insert(0, numbers[i - 1][0] - numbers[i][0])
        result += numbers[0][0]
    return result
