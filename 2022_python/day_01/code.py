

path = "2022_python/day_01/input.txt"
with open(path) as f:
        lines = [x.rstrip() for x in f]

# Part 1
max_elf = 0
current_elf = 0
for x in lines:
    if x == "":
        max_elf = current_elf if current_elf > max_elf else max_elf
        current_elf = 0
    else:
        current_elf = current_elf + int(x)

max_elf

# Part 2
elves = []
current_elf = 0
for x in lines:
    if x == "":
        elves.append(current_elf)
        current_elf = 0
    else:
        current_elf = current_elf + int(x)

sum(sorted(elves, reverse=True)[0:3])