import numpy as np
from collections import Counter

test = np.array([3,4,3,1,2])
input = np.loadtxt("python/aoc_2021/inputs/day06-1.txt", delimiter=",")

# A function that does the population cycle. 
def pop_cycle(state):
    zeros = sum(state == 0) # count the number of 0s
    state -= 1 # increment
    state = state[state >= 0] # remove negatives
    if zeros > 0:
        state = np.append(state, [6] * zeros) # Add 6s in
        state = np.append(state, [8] * zeros) # Add 8s in
    return state


# Loop over in a while loop
# This gets very slow, as there are a lot of fish!
# Might be interesting to re-implement with a counter or a dict somehow?
# Basically, the numbers in the dict shift by 1 every time, and then we add outgoing 0s to 6s and 8s
target_days = 80
day = 0
state = np.copy(test) # works with test data
state = np.copy(input) # works with test data
while day < target_days:
    print(f"After {day} days: {len(state)} fish")
    print(state)
    state = pop_cycle(state)
    day += 1

len(state)

# Part 2
# My comment above may have forshadowed this...
# Now, they want it to run for 256 days
# Can try this on the test data and see if it works:
# But it doesn't... Or at least, it is very slow. 
# So, let's try again, but using Counter and dicts


# A function to cycle populations using a counter
def pop_cycle_dict(state):
    default = Counter(dict.fromkeys(range(9), 0))
    zeros = state[0] # get the current number of zeros. This will be the number we add to 6 and 8
    # Get a dictionary for updating, by shifting all keys by one
    new_state = Counter({key - 1: item for key, item in zip(state.keys(), state.values())})
    new_state.pop(-1) # remove the negative values
    update_dict = Counter({6: zeros, 8: zeros})
    # Do updates and return new state
    default.update(new_state) # .update() with counters adds instead of replacing, which is why we set default to 0 above
    default.update(update_dict)
    return default


# Set the initial state
state = Counter(dict.fromkeys(range(9), 0))
state.update(Counter(input))
target_days = 256
day = 0
while day < target_days:
    state = pop_cycle_dict(state)
    day += 1

state
sum(list(state.values()))
