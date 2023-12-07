import contextlib


def calc(lines: list[str]) -> int:
    numbers = []
    for i, line in enumerate(lines):
        next_num = ""
        is_sym_near = False
        for j, letter in enumerate(line):
            if letter.isdigit():
                next_num = f"{next_num}{letter}"
                if is_sym_near:
                    continue
                edge_syms = ""
                for k, g in [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j + 1),
                    (i + 1, j),
                ]:
                    with contextlib.suppress(IndexError):
                        edge_syms += lines[k][g]
                edge_syms = edge_syms.replace(".", "")
                if edge_syms and not edge_syms.isdigit():
                    is_sym_near = True
            elif next_num:
                if is_sym_near:
                    numbers.append(int(next_num))
                next_num = ""
                is_sym_near = False
        if next_num and is_sym_near:
            numbers.append(int(next_num))
    return sum(numbers)
