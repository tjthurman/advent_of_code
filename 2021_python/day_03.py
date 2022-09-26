from collections import Counter
path = "python/aoc_2021/inputs/day03-1.txt"
with open(path) as f:
    output = [x.rstrip() for x in f]

gamma_bits = []
for position in range(len(output[0])):
    counts = Counter([line[position] for line in output])
    print(counts)
    max_index = list(counts.values()).index(max(counts.values()))
    bit = list(counts.keys())[max_index]
    gamma_bits.append(bit)

gamma_rate = int("".join(gamma_bits), 2)

# Epsilon rate is the opposite
episilon_bits = [str(int(not bool(int(bit)))) for bit in gamma_bits]
epsilon_rate = int("".join(episilon_bits), 2)

gamma_rate*epsilon_rate

# Part 2
possibilities = list(output)
cur_pos = 0
while len(possibilities) > 1:
    counts = Counter([line[cur_pos] for line in possibilities])
    if counts["1"] == counts["0"]:
        choice = "1"
    elif counts["1"] > counts["0"]:
        choice = "1"
    else:
        choice = "0"
    possibilities = list([x for x in possibilities if x[cur_pos] == choice])
    cur_pos += 1

oxy_gen_rating = int(possibilities[0], 2)


# Don't love the repetition.
# Would be nice to think of a better way. 
possibilities = list(output)
cur_pos = 0
while len(possibilities) > 1:
    counts = Counter([line[cur_pos] for line in possibilities])
    if counts["1"] == counts["0"]:
        choice = "0"
    elif counts["1"] > counts["0"]:
        choice = "0"
    else:
        choice = "1"
    possibilities = list([x for x in possibilities if x[cur_pos] == choice])
    cur_pos += 1
        
scrubber_rating = int(possibilities[0], 2)

oxy_gen_rating*scrubber_rating
