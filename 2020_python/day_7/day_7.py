import re

with open("day_7/input.txt") as f:
    rules = f.read().splitlines()


def get_outer_bag(rule):
    outer = rule.split("bags contain")[0].replace(" ", "")
    return outer

def get_inner_bags(rule):
    right = re.sub(r'bags?.', r'', re.sub(r'bags?,', r'', rule.split("bags contain")[1]))
    inner = [x.replace(" ", "") for x in re.split(r'\s?\d\s?', right)][1:]
    return inner

# Using those functions, assemble a dictionary of outer and inner bags
x = {get_outer_bag(rule):get_inner_bags(rule) for rule in rules}



# First iteration
possible_outer_bags = set([outer_bag for outer_bag in list(x.keys()) if "shinygold" in x[outer_bag]])

# Then, iterate over the possible outer bags until we're no longer
# adding new candidates
old_len = 0
new_len = len(possible_outer_bags)
while (new_len - old_len) != 0:
    old_len = new_len
    for poss_out_bag in list(possible_outer_bags):
        possible_outer_bags = possible_outer_bags.union(set([outer_bag for outer_bag in list(x.keys()) if poss_out_bag in x[outer_bag]]))
    new_len = len(possible_outer_bags)

# And get the length
len(possible_outer_bags)

# Part 2
# Now we want the number of the inner bags, as I expected
# So, we let's make a dict, where this the key is the outer bag, but this time the
# value is not a list of colors, but instead a dict where the colors are the keys and the numbers are the values
# so, the outer bag function stays the same
# Need a new iner bag function
import numpy as np

def get_inner_bags_and_numbers(rule):
    right = re.sub(r'bags?.', r'', re.sub(r'bags?,', r'', rule.split("bags contain")[1]))
    inner_colors = [x.replace(" ", "") for x in re.split(r'\s?\d\s?', right)][1:]
    inner_numbers = list(re.sub(r'\D', r'', right))
    if len(inner_numbers) > len(inner_colors):
        print("Number color mismatch")
        return False
    inner = dict(zip(inner_colors, inner_numbers))
    return inner

with open("day_7/example_1.txt") as f:
    rules = f.read().splitlines()

with open("day_7/example_2.txt") as f:
    rules = f.read().splitlines()

with open("day_7/input.txt") as f:
    rules = f.read().splitlines()


# Assemble the rules into a list of dicts
x = {get_outer_bag(rule):get_inner_bags_and_numbers(rule) for rule in rules}

# Could also get a dict of number of bags within each color:
bags_per_color = {get_outer_bag(rule):sum([int(num) for num in list(get_inner_bags_and_numbers(rule).values())]) for rule in rules}
    
    

def all_bags_within(bag_color):
    if bags_per_color[bag_color] == 0:
        bags = 0
    else:
        colors_inside = list(x[bag_color].keys())
        numbers_inside = [int(num) for num in list(x[bag_color].values())]
        multipliers = [all_bags_within(color) for color in colors_inside]
        bags = sum(np.multiply(numbers_inside, multipliers)) + sum(numbers_inside)
    return bags


all_bags_within("shinygold")
