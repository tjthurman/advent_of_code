import itertools
from collections import Counter

test_path = "python/aoc_2021/inputs/day08-test.txt"
path = "python/aoc_2021/inputs/day08-1.txt"



with open(test_path) as f:
    test = [x.rstrip() for x in f]

with open(path) as f:
    input = [x.rstrip() for x in f]

# Get the seonc half of the input
four_digits = [line.split(" | ")[1] for line in input]
# Nested list comprehension to count the number of segments in each set of digits
seg_numbers = [[len(segments) for segments in line.split(" ")] for line in four_digits]

# Flatten the list and count up the 2s, 4s, 3s, and 6s
sum([x in [2,4,3,7] for x in list(itertools.chain(*seg_numbers))])
# That worked with the test data, repeat with real data

# Part 2
# This looks much, much more complicated. 
# Let's build up the logic
# I'll use the wikipedia article to do the encoding
# With each segment getting a capital A-G
# They also have a nice table, which I can look at for some deductions
# First, a dictionary giving the sorted segments that make up each letter
seg_to_number = {"ABCDEF": 0, "BC": 1, "ABDEG": 2, 
                 "ABCDG": 3, "BCFG": 4, "ACDFG": 5,
                 "ACDEFG": 6, "ABC": 7, "ABCDEFG": 8, 
                 "ABCDFG": 9}

# And a help function to flatten lists
def flatten_list(in_list): 
    return list(itertools.chain(*in_list))

# An ungodly function to do all the logic:
# outputs a dict where the keys are the segments from the signal
# and the valus are the segment locations
def decode_signals(signals):
    known_segments = dict.fromkeys(["a", "b", "c", "d", "e", "f", "g"], None)
    sorted = [set(list(string)) for string in signals]
    lengths = [len(list) for list in sorted]
    # Grab the segment signals for the unique numbers
    one_segs = sorted[lengths.index(2)]
    four_segs = sorted[lengths.index(4)]
    seven_segs = sorted[lengths.index(3)]
    eight_segs = sorted[lengths.index(7)]
    # Can compare 1 and seven to get the value for segment A
    known_segments["".join(seven_segs.difference(one_segs))] = "A"
    # can count up how often each signal appears
    # some segments appear a unique number of times in the set of numbers
    counts = Counter(flatten_list(sorted))
    known_segments[list(counts.keys())[list(counts.values()).index(9)]] = "C"
    known_segments[list(counts.keys())[list(counts.values()).index(6)]] = "F"
    known_segments[list(counts.keys())[list(counts.values()).index(4)]] = "E"
    # Once we know C, can figure out B
    for key in list(one_segs):
        if (known_segments[key] is None):
            known_segments[key] = "B"
    # Can figure out G: it is the unknown one in 4
    for key in list(four_segs):
        if (known_segments[key] is None):
            known_segments[key] = "G"
    # Remaining one in 8 is D
    for key in list(eight_segs):
        if (known_segments[key] is None):
            known_segments[key] = "D"
    return known_segments
    

# Given a key, convert a set of signals
# to the digits
def convert_digits(key, digits):
    out_digits = []
    for input_signal in digits.split(" "):
        segments = [key[letter] for letter in str(input_signal)]
        segments.sort()
        digit = seg_to_number["".join(segments)]
        out_digits.append(digit)
    return out_digits

# Put it all together in a loop to get the answer
final_res = []
for line in input:
    signal = line.split(" | ")[0]
    digits = line.split(" | ")[1]
    key = decode_signals(signal.split(" "))
    result = convert_digits(key, digits)
    num_result = int("".join(str(x) for x in result))
    final_res.append(num_result)


sum(final_res)

