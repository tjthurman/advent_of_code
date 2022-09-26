
## Puzzle 1
# Read in the input data
with open("day_1/puzzle_1/input.txt") as f:
    inData = f.read().splitlines()

# Need to find the two numbers in this data that add up to 2020
# Can just take 2020 - the input data to get the differences for every item
diffs = [str(2020 - int(x)) for x in inData]

# And find the interesction of the two lists to find the two elements that add up to 2020
pair = set.intersection(set(inData), set(diffs))

# Multiply to get the result
result = int(list(pair)[0]) * int(list(pair)[1])

## Puzzle 2
# Now, we need to find the THREE entries that sum up to 2020
with open("day_1/puzzle_1/input.txt") as f:
    inData = f.read().splitlines()

# Let's abstract the idea above, making it find the proper pair for any
# given goal number
def find_diff_pair(goal_sum, input_list):
    diffs = [str(goal_sum - int(x)) for x in input_list]
    pair = set.intersection(set(input_list), set(diffs))
    return pair


# Then, a little loop.
# We set up an empty set
three = set()
# Then we loop over the list of 2020 - input data,
# using those differences as the new goal target in our function
# to find a pair of numbers.
# Then we take the union of all those sets (most of which are empty)
# to get our set of three
for x in [str(2020 - int(x)) for x in inData]:
   three=three.union(find_diff_pair(int(x), inData))

# Then multiply them to get our result
int(list(three)[0]) * int(list(three)[1]) * int(list(three)[2])