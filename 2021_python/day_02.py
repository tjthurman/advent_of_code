path = "python/aoc_2021/inputs/day02-1.txt"
with open(path) as f:
    commands = [x.rstrip() for x in f]

# Part 1
depth = []
pos = []
for line in commands:
    if line.split()[0] in ["up", "down"]:
        depth.append(line)
    else:
        pos.append(line)

final_pos = sum([int(line.split()[1]) for line in pos])

final_depth = sum([int(line.split()[1]) if line.split()[0] == "down" else int(line.split()[1])*-1 for line in depth])

final_pos * final_depth


# part 2
def get_sign(command):
    if command.split()[0] in ["down", "forward"]:
        sign = 1
    else:
        sign = -1
    return sign

def get_aim_change(command):
    if command.split()[0] in ["up", "down"]:
        change = int(command.split()[1])
    else:
        change = 0
    return change


aim = 0
depth = 0
pos = 0
for line in commands:
    sign = get_sign(line)
    aim_change = get_aim_change(line)
    aim += aim_change*sign
    if line.split()[0] == "forward":
        depth += aim*int(line.split()[1])
        pos += int(line.split()[1])

pos*depth





[get_sign(line) for line in commands]