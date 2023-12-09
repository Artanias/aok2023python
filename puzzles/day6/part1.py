def calc(lines: list[str]) -> int:
    _, times = lines[0].split(":")
    times = map(int, times.split())
    _, distances = lines[1].split(":")
    distances = map(int, distances.split())
    result = 1
    for time, distance in zip(times, distances):
        result *= sum(1 for i in range(1, time) if (time - i) * i > int(distance))
    return result
