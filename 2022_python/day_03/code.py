
import string

path = "2022_python/day_03/test.txt"
with open(path) as f:
       test_data = [x.rstrip() for x in f]

path = "2022_python/day_03/input.txt"
with open(path) as f:
       real_data = [x.rstrip() for x in f]

# Part 1
# First, a function to get the item score
def item_score(letter):
    scores = {key:value for (key, value) in zip(list(string.ascii_letters), list(range(1, 53)))}
    return scores[letter]

rucksack = test_data[0]

def rucksack_priority(ruck_string):
    # Divide in half
    # while converting to sets to get uniq letters
    midpoint = int(len(ruck_string)/2)
    first_half = set(list(ruck_string[:midpoint]))
    second_half = set(list(ruck_string[midpoint:]))
    # get common item
    common_item = first_half.intersection(second_half)
    # Return the priority for that item
    return item_score("".join(list(common_item)))

sum([rucksack_priority(item) for item in test_data]) == 157

sum([rucksack_priority(item) for item in real_data])

# Part 2
# Now do by group
import itertools
from functools import reduce

itertools.groupby(test_data, lambda x: x[0:2])

def my_intersect(string1, string2):
    set1 = set(list(string1))
    set2 = set(list(string2))
    return(set1.intersection(string2))

def group_priority(rucksack_list):
    common_item = reduce(my_intersect, rucksack_list)
    return item_score("".join(list(common_item)))

# Had to google this little group by trick
sum([group_priority(group) for group in zip(*(iter(test_data),) * 3)]) == 70
sum([group_priority(group) for group in zip(*(iter(real_data),) * 3)])

# Without the group by trick
def score_by_group(rucksack_list):
    group_scores = []
    for i in range(0, len(rucksack_list), 3):
        group_score = group_priority(rucksack_list[i:(i+3)])
        group_scores.append(group_score)
    return group_scores

sum(score_by_group(test_data))
sum(score_by_group(real_data))