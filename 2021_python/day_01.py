
from lib2to3.pytree import _Results


path = "python/aoc_2021/inputs/day01-1.txt"
with open(path) as f:
    lines = [int(x.rstrip()) for x in f]

# Part 1
sum([value > lines[index - 1] for index, value in enumerate(lines)])


# Part 2, do in a sliding window
winsize = 3
# calculate all the sliding windows
win_sums = [sum(lines[index:(index + winsize)]) for index in range(len(lines)-winsize +1)]
# then do the same thing as before
sum([value > win_sums[index - 1] for index, value in enumerate(win_sums)])
