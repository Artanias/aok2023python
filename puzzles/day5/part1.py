from copy import copy


def calc(lines: list[str]) -> int:
    _, seeds = lines.pop(0).split(": ")
    map_seeds = {}
    seed_to_loc = {int(num): int(num) for num in seeds.split()}
    curr_map_key = ""
    map_keys = []
    for line in lines:
        if not line:
            continue
        if line.endswith(":"):
            curr_map_key = line[:-1].split()[0]
            map_keys.append(curr_map_key)
            map_seeds[curr_map_key] = []
            continue
        dest_range_start, src_range_start, range_length = map(
            int, line.split(maxsplit=2)
        )
        map_seeds[curr_map_key].append(
            (
                range(src_range_start, src_range_start + range_length),
                range(dest_range_start, dest_range_start + range_length),
            )
        )
    for key in map_keys:
        curr_map = map_seeds[key]
        curr_seed_to_loc = copy(seed_to_loc)
        for src_range, dest_range in curr_map:
            for seed, value in curr_seed_to_loc.items():
                if value not in src_range:
                    continue
                seed_to_loc[seed] = dest_range.start + (value - src_range.start)
    return min(val for val in seed_to_loc.values())
