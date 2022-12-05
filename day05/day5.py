import re
from utils import readinput

matcher = re.compile("move (\d+) from (\d+) to (\d+)")


def make_crate(lines, index):
    r = list()
    for line in lines:
        idx = 1 + (index * 4)
        if line[idx] != ' ':
            r.append(line[idx])
    return r


def parse_move(move):
    match = matcher.match(move)
    num = int(match.group(1))
    from_crate = int(match.group(2)) - 1
    to_crate = int(match.group(3)) - 1
    return num, from_crate, to_crate


def part1():
    lines = readinput(strip=False)
    crates = [make_crate(lines[:8], i) for i in range(9)]
    moves = lines[10:]

    for move in moves:
        num, from_crate, to_crate = parse_move(move)
        for i in range(num):
            tmp = crates[from_crate].pop(0)
            crates[to_crate].insert(0, tmp)

    return ''.join(crate[0] for crate in crates)


def part2():
    lines = readinput(strip=False)
    crates = [make_crate(lines[:8], i) for i in range(9)]
    moves = lines[10:]

    for move in moves:
        num, from_crate, to_crate = parse_move(move)
        moving = crates[from_crate][:num]
        crates[from_crate] = crates[from_crate][num:]
        crates[to_crate] = moving + crates[to_crate]

    return ''.join(crate[0] for crate in crates)


print(part1())
print(part2())
