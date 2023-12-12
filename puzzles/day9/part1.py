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
            numbers[i - 1].append(numbers[i][-1] + numbers[i - 1][-1])
        result += numbers[0][-1]
    return result
