
from utils import readinput


def part1():
    def overlaps(a1, a2, b1, b2):
        if a1 >= b1 and a2 <= b2:
            return True
        if b1 >= a1 and b2 <= a2:
            return True
        return False

    total = 0
    lines = readinput()
    for line in lines:
        a, b = line.split(',')
        a1, a2 = a.split('-')
        a1 = int(a1)
        a2 = int(a2)
        b1, b2 = b.split('-')
        b1 = int(b1)
        b2 = int(b2)
        if overlaps(a1, a2, b1, b2):
            total += 1

    return total


def part2():

    def overlaps(a1, a2, b1, b2):
        if (a2 < b1 and a2 < b2) or (b2 < a1 and b2 < a2):
            return False
        return True

    total = 0
    lines = readinput()
    for line in lines:
        a, b = line.split(',')
        a1, a2 = a.split('-')
        a1 = int(a1)
        a2 = int(a2)
        b1, b2 = b.split('-')
        b1 = int(b1)
        b2 = int(b2)
        if overlaps(a1, a2, b1, b2):
            total += 1

    return total


print(part1())
print(part2())
