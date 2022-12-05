
from utils import readinput


def part1():
    total = 0
    lines = readinput()
    for line in lines:
        half = int(len(line) / 2)
        first = line[:half]
        second = line[half:]
        common = set(first).intersection(set(second)).pop()
        if ord(common) >= 97:
            value = ord(common) -96
        else:
            value = ord(common) - 38
        total += value
    return total


def part2():
    total = 0
    lines = readinput()
    groups = []
    group = []
    for line in lines:
        if len(group) < 3:
            group.append(line)
        if len(group) == 3:
            groups.append(group)
            group = []

    for group in groups:
        common = set(group[0]).intersection(set(group[1]).intersection(set(group[2]))).pop()
        if ord(common) >= 97:
            value = ord(common) -96
        else:
            value = ord(common) - 38
        total += value
    return total


print(part1())
print(part2())
