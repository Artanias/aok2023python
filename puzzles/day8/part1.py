def calc(lines: list[str]) -> int:
    instructions = lines.pop(0)
    move_map = {}
    for line in lines:
        if not line:
            continue
        pos, left_right = line.split(" = ", maxsplit=1)
        left, right = left_right[1:-1].split(", ", maxsplit=1)
        move_map[pos] = {}
        move_map[pos]["left"] = left
        move_map[pos]["right"] = right
    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current_node = move_map[current_node]["left"]
            else:
                current_node = move_map[current_node]["right"]
            steps += 1
            if current_node == "ZZZ":
                return steps
