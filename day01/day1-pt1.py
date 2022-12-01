from utils import readgroups, to_ints

elves = readgroups('input.txt')
elves = [sum(to_ints(elf)) for elf in elves]
print(max(elves))
