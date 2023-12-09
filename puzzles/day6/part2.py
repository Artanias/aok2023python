def calc(lines: list[str]) -> int:
    _, time = lines[0].split(":")
    time = int(time.replace(" ", ""))
    _, distance = lines[1].split(":")
    distance = int(distance.replace(" ", ""))
    result = sum(1 for i in range(1, time) if (time - i) * i > int(distance))
    return result
