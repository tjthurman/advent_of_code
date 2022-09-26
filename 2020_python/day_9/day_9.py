import numpy as np

# Part 1
with open("day_9/input.txt") as f:
    input =  [int(x) for x in f.read().splitlines()]



def calc_valid_numbers(input):
    valid_numbers = list()
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j:
                break
            else:
                valid_numbers.append(input[i] + input[j])
    return list(set(valid_numbers))

for count, value in enumerate(input):
    if count > 24:
        possible_values = calc_valid_numbers(input[count-25:count])
        current = value
        if current not in possible_values:
            print(current)

# Part 2
target_number = 556543474

for count, value in enumerate(input):
    cumulative_sums = list(np.cumsum(input[count:]))
    if target_number in cumulative_sums:
        contig_run = input[count:count + cumulative_sums.index(target_number) + 1]
        print(min(contig_run) + max(contig_run))