from copy import copy


def src_range_num_to_dest(number: int, src_range: range, dest_range: range):
    return dest_range.start + (number - src_range.start)


def calc(lines: list[str]) -> int:
    _, seeds = lines.pop(0).split(": ")
    map_seeds = {}
    seeds_nums = [int(num) for num in seeds.split()]
    ranges = []
    for start_range, cnt_el in zip(seeds_nums[::2], seeds_nums[1::2]):
        ranges.append(range(start_range, start_range + cnt_el))
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
    not_handled_ranges = copy(ranges)
    for key in map_keys:
        curr_map = map_seeds[key]
        new_ranges = []
        while not_handled_ranges:
            for range_ in copy(not_handled_ranges):
                if all(
                    [
                        (
                            range_.start not in src_range
                            and (range_.stop - 1) not in src_range
                        )
                        for src_range, _ in curr_map
                    ]
                ):
                    new_ranges.append(range_)
                    not_handled_ranges.remove(range_)
            for src_range, dest_range in curr_map:
                for range_ in copy(not_handled_ranges):
                    if src_range.start > (range_.stop - 1):
                        continue
                    elif (src_range.stop - 1) < range_.start:
                        continue
                    # full match
                    elif (
                        src_range.start <= range_.start
                        and src_range.stop >= range_.stop
                    ):
                        not_handled_ranges.remove(range_)
                        new_ranges.append(
                            range(
                                src_range_num_to_dest(
                                    range_.start, src_range, dest_range
                                ),
                                src_range_num_to_dest(
                                    range_.stop, src_range, dest_range
                                ),
                            )
                        )
                    # left match
                    elif (
                        src_range.start < range_.start
                        and (src_range.stop - 1) in range_
                    ):
                        not_handled_ranges.remove(range_)
                        new_ranges.append(
                            range(
                                src_range_num_to_dest(
                                    range_.start, src_range, dest_range
                                ),
                                src_range_num_to_dest(
                                    src_range.stop, src_range, dest_range
                                ),
                            )
                        )
                        not_handled_ranges.append(range(src_range.stop, range_.stop))
                    # right match
                    elif src_range.start in range_ and src_range.stop > range_.stop:
                        not_handled_ranges.remove(range_)
                        new_ranges.append(
                            range(
                                src_range_num_to_dest(
                                    src_range.start, src_range, dest_range
                                ),
                                src_range_num_to_dest(
                                    range_.stop, src_range, dest_range
                                ),
                            )
                        )
                        not_handled_ranges.append(range(range_.start, src_range.start))
                    else:
                        not_handled_ranges.remove(range_)
                        new_ranges.append(
                            range(
                                src_range_num_to_dest(
                                    src_range.start, src_range, dest_range
                                ),
                                src_range_num_to_dest(
                                    src_range.stop, src_range, dest_range
                                ),
                            )
                        )
                        if range_.stop > src_range.stop:
                            not_handled_ranges.append(
                                range(src_range.stop, range_.stop)
                            )
                        else:
                            not_handled_ranges.append(
                                range(range_.start, src_range.start)
                            )
        not_handled_ranges = copy(new_ranges)
        ranges = new_ranges
    return min(range_.start for range_ in ranges)
