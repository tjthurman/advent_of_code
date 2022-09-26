# Down the slope

with open("day_3/map.txt") as f:
    lines = f.read().splitlines()

# Start location
location = 0
row = 0

# Tree counter
trees = 0


for line in lines:
    # Figure out the index within the string
    index = (row*3) % len(line)

    # show = list(line)
    # show[index] = "X"
    # print(''.join(show))

    if line[index] == '#':
        trees += 1
    
    # Change position
    row += 1
    location += 3

trees

# Part 2

# Now that I've figured it out above, can simplify a little

def count_trees(down, right, map):
    trees = 0
    step = 0
    for row in list(range(0, len(map), down)): # get the indices of the rows I want
        index = (step*right) % len(line) # Figure out how far to the right to go (based on step, not row)
        if map[row][index] == '#': # Check for a tree
            trees += 1
        step += 1 # Increment the step count (steps != rows)
    return trees


# Do each slope
a = count_trees(down = 1, right = 1, map = lines)
b = count_trees(down = 1, right = 3, map = lines)
c = count_trees(down = 1, right = 5, map = lines)
d = count_trees(down = 1, right = 7, map = lines)
e = count_trees(down = 2, right = 1, map = lines)

# Multiply
a*b*c*d*e