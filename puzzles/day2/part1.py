POSSIBLE_CNT = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def calc(lines: list[str]) -> int:
    result = 0
    for line in lines:
        game, subsets = line.split(":", maxsplit=1)
        game_num = int(game.split()[-1])
        game_possible = True
        for subset in subsets.split(';'):
            game_cnt = {"red": 0, "green": 0, "blue": 0}
            for cube in subset.split(','):
                cnt, color = cube.strip().split()
                game_cnt[color] += int(cnt)
            if any(game_cnt[color] > POSSIBLE_CNT[color] for color in game_cnt):
                game_possible = False
                break
        if not game_possible:
            continue
        result += game_num
    return result
