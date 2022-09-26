import numpy as np
test = [16,1,2,0,4,2,7,1,2,14]
input = np.loadtxt("python/aoc_2021/inputs/day07-1.txt", delimiter=",")

# calculate fuel spends for all possible positions
fuel = {pos: sum(np.abs(np.array(input) - pos))  for pos in range(int(max(input)) + 1)}
# Find minimum fuel
min(fuel.values())

# Part 2
# now fuel cost is different. A function to get the cost for a given offset
# This is the naive way to do this.
# But, takes absolutely forever
def cost(number):
    fuel = 0
    while number > 0:
        fuel += number
        number -= 1
    return fuel

# Some quick googling shows that there is an easy formula for this:
def cost2(number):
    return number*(number + 1)/2

# And to apply that function across a list of offsets
# Very, very slow. Would be nice to think of ways to fix. Memoize fuel costs?
# There's probably some optimization functions I could use in some math libraries,
# using a different equation as a cost function. 
def fuel_cost(array):
    out = [None] * len(array)
    for index, value in enumerate(array):
        out[index] = cost2(value) # with this cost function, very fast
    return np.array(out)

fuel = {pos: sum(fuel_cost(np.abs(np.array(input) - pos)))  for pos in range(int(max(input)) + 1)}

min(fuel.values())


