
import numpy as np

# Part 1
# Read in the adaptors
with open("day_10/input.txt") as f:
    adaptors = np.array([int(x) for x in f.read().splitlines()])

# Add the effective joltage of the outlet to the list
adaptors = np.append(adaptors, 0)

# Sort, take cumulative difference, and count up values all in one step
counts = np.unique(np.diff(np.sort(adaptors)), return_counts=True)[1]

# Multiply the 1s by the 3s, adding 1 to three (since my built in adaptor is 3 more than the max)
counts[0]*(counts[1] + 1)

# Part 2

# My intuition here is that what matters is the number of differences of 1 in a row
# A 1 followed by a one means that you could either keep, or not, the first one. 
# Lets use the examples to start figuring that out

with open("day_10/example_1.txt") as f:
    adaptors = np.array([int(x) for x in f.read().splitlines()])

adaptors = np.append(adaptors, 0)
diffs = np.diff(np.sort(adaptors))
len(diffs)
# Yes, there are 3 times where a 1 is followed by a 1, leading to:
2**3 # 8 different ways

with open("day_10/example_2.txt") as f:
    adaptors = np.array([int(x) for x in f.read().splitlines()])

adaptors = np.append(adaptors, 0)
diffs = np.diff(np.sort(adaptors))
len(diffs)

# applying the naive possible combos = 2**(i-1), where i == # of ones in a row
opportunities = 0
index = 1
max_index = len(diffs)
for adaptor in diffs:
    if int(index) == max_index:
        break
    if adaptor == 1:
        if diffs[index - 1 ] == 1:
            opportunities += 1
    index += 1
# Doesn't quite work. 

# This gets us the right answer
7**4 * 4 * 2

# So, the above turns out to be not quite right:
# for 2 1 in a row, there are 2 possible combos
# for 3 1 in a row, there are 4 possible combos
# for 4 1 in a row, there are **7** possible combos. 
# To be honest, can't quite figure out what the pattern is there, so I don't know how many 5 
# 1 in a row combos there'd be. Looks like I don't need to, as my dataset doesn't include that. But might be nice to figure out:
# for 5 i in a row, looks like 14 combinations?
# Not gonna try 6 in a row, but my guess is it would be 29? Seems like this is the formula for
# the number of possible ways give i 1s in a row, given that i is at least 3:
# 2**(i -1) - (i - 3)

# In any case, let's move on to figuring out the number of possibilities in my input data.
# Need to take my input diffs and count the # of times there a 4, 3, and 2 is in a row:
with open("day_10/input.txt") as f:
    adaptors = np.array([int(x) for x in f.read().splitlines()])

# Add the effective joltage of the outlet to the list
adaptors = np.append(adaptors, 0)

# Get the diffs
diffs = np.diff(np.sort(adaptors))

index = 0
results = list()
counter = 0
while index < len(diffs):
    if index == len(diffs) - 1: # If at the end
        counter += 1 # increment counter
        results.append(counter) # add to results
        # and finish
        break
    # while not at the end
    if diffs[index] == 1:
        counter += 1
    else:
        results.append(counter)
        counter = 0
    index += 1
counts = np.unique(np.array(results), return_counts=True)[1]

# Get answer:
7**counts[4] * 4**counts[3] * 2**counts[2]


# Exploring other people's solutions:
from collections import Counter
import fileinput

with open("day_10/input.txt") as f:
    adaptors = f.read().splitlines()

def part2(lines):
    '''
    >>> part2(list(map(str, (16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4))))
    8
    >>> part2(list(map(str, (28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3))))
    19208
    '''
    nums = sorted(map(int, lines))
    counter = Counter((0, ))
    for num in nums:
        counter[num] += sum(counter[i] for i in range(num - 3, num))
    return counter[nums[-1]]

    # This counter library looks very useful for these types of challenges
    
