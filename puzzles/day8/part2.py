import math


def is_all_ends_with_z(nodes: list[str]) -> bool:
    return all(node.endswith("Z") for node in nodes)


def calc(lines: list[str]) -> int:
    instructions = lines.pop(0)
    move_map = {}
    start_nodes = []
    for line in lines:
        if not line:
            continue
        pos, left_right = line.split(" = ", maxsplit=1)
        left, right = left_right[1:-1].split(", ", maxsplit=1)
        if pos.endswith("A"):
            start_nodes.append(pos)
        move_map[pos] = {}
        move_map[pos]["left"] = left
        move_map[pos]["right"] = right
    steps_to_z = []
    for node in start_nodes:
        current_node = node
        steps = 0
        while not current_node.endswith("Z"):
            for instruction in instructions:
                if instruction == "L":
                    current_node = move_map[current_node]["left"]
                else:
                    current_node = move_map[current_node]["right"]
                steps += 1
        steps_to_z.append(steps)
    return math.lcm(*steps_to_z)
