from collections import Counter
import itertools

test_path = "python/aoc_2021/inputs/day05-test.txt"
path = "python/aoc_2021/inputs/day05-1.txt"

# Load the example data for testing
with open(test_path) as f:
    test = [x.rstrip() for x in f]

# and the real data
with open(path) as f:
    input = [x.rstrip() for x in f]

# A function to parse the input into a list of x1, x2, y1, y2
def parse_input(input):
    tmp = input.split(" -> ")
    x1 = int(tmp[0].split(",")[0])
    x2 = int(tmp[1].split(",")[0])
    y1 = int(tmp[0].split(",")[1])
    y2 = int(tmp[1].split(",")[1])
    return [x1, x2, y1, y2]

parsed_test = [parse_input(line) for line in test]

def get_points(parsed_input):
    if parsed_input[0] == parsed_input[1]: # Xs equal, vertical line
        y_coords = sorted(parsed_input[2:])
        return [[parsed_input[0], y_coord] for y_coord in range(y_coords[0], y_coords[1] + 1)]
    elif parsed_input[2] == parsed_input[3]: # Ys equal, horizontal line
        x_coords = sorted(parsed_input[0:2])
        return [[x_coord, parsed_input[2]] for x_coord in range(x_coords[0], x_coords[1] + 1)]
    else: # diagonal line, return empty points for now
        return []

all_points = [get_points(x) for x in parsed_test]

# This flattens the list, and then converts the list of points to a string
# so that I can count it. 
points_flat = [str(x) for x in list(itertools.chain(*all_points))]
# Then do a counter, and count the number of elements with >= 2
answer = sum([x >= 2 for x in list(Counter(points_flat).values())])

# Got the right answer on the test data, so let's try it with the actual data
parsed_input = [parse_input(line) for line in input]
all_points = [get_points(x) for x in parsed_input]
points_flat = [str(x) for x in list(itertools.chain(*all_points))]
answer = sum([x >= 2 for x in list(Counter(points_flat).values())])
# Correct!

# Part two
# Now, need to add in diagonal lines, as expected
# So, let's revisit the get_points function
def get_points2(parsed_input):
    if parsed_input[0] == parsed_input[1]: # Xs equal, vertical line
        y_coords = sorted(parsed_input[2:])
        return [[parsed_input[0], y_coord] for y_coord in range(y_coords[0], y_coords[1] + 1)]
    elif parsed_input[2] == parsed_input[3]: # Ys equal, horizontal line
        x_coords = sorted(parsed_input[0:2])
        return [[x_coord, parsed_input[2]] for x_coord in range(x_coords[0], x_coords[1] + 1)]
    else: # diagonal line
        x_coords = parsed_input[0:2]
        y_coords = parsed_input[2:]
        x_dir = 1 if x_coords[0] < x_coords[1] else -1
        y_dir = 1 if y_coords[0] < y_coords[1] else -1
        x_range = range(x_coords[0], x_coords[1] + x_dir, x_dir)
        y_range = range(y_coords[0], y_coords[1] + y_dir, y_dir)
        return [[x_coord, y_coord] for x_coord, y_coord in zip(x_range, y_range)]

parsed_input = [parse_input(line) for line in input]
all_points = [get_points2(x) for x in parsed_input]
points_flat = [str(x) for x in list(itertools.chain(*all_points))]
answer = sum([x >= 2 for x in list(Counter(points_flat).values())])