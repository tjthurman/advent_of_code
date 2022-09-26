import numpy as np

test_path = "python/aoc_2021/inputs/day09-test.txt"
path = "python/aoc_2021/inputs/day09-1.txt"


with open(test_path) as f:
    test = [x.rstrip() for x in f]
with open(path) as f:
    input = [x.rstrip() for x in f]

test_arr = np.array([list(map(int, str(line))) for line in test])
input_arr = np.array([list(map(int, str(line))) for line in input])

low_points = []
dims = input_arr.shape
array = input_arr.copy()
risk_levels = []
for row in range(dims[0]):
    for col in range(dims[1]):
        if row == 0:
            top = 11
        else:
            top = array[row - 1, col]
        if row == dims[0] - 1:
            bottom = 11
        else:
            bottom = array[row + 1, col]
        if col == 0:
            left = 11
        else:
            left = array[row, col -1]
        if col == dims[1] -1:
            right = 11
        else:
            right = array[row, col + 1]
        if sum([array[row, col] < side for side in [top, right, bottom, left]]) == 4:
            risk_levels.append(array[row, col] + 1)
    


sum(risk_levels)

# Part 2

data = test_arr.copy()


basin_ids = np.arange(data.shape[0] * data.shape[1]).reshape(data.shape) + 1
is_basin = data < 9
basin_ids[~is_basin] = 0

np.maximum(basin_ids[:-1], basin_ids[1:])
