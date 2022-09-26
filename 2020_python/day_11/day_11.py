# Part 1

import collections
import copy

with open("day_11/example.txt") as f:
    lines =  f.read().splitlines()
    example = [list(x) for x in lines]

with open("day_11/input.txt") as f:
    lines =  f.read().splitlines()
    input = [list(x) for x in lines]



# Dimensions in rows, columns
def dimensions(input_text_grid):
    return [len(input_text_grid), len(input_text_grid[0])]




def get_adjacent_tiles(input_grid, x_coord, y_coord):
    dim = dimensions(input_grid)

    # Get starting x position
    if x_coord == 0:
        x_start = 0
    else:
        x_start = x_coord -1 
    # Get ending x_position
    if x_coord == dim[1] -1:
        x_end = x_coord
    else:
        x_end = x_coord + 1

    # Get starting y position
    if y_coord == 0:
        y_start = 0
    else:
        y_start = y_coord -1 
    # Get ending y_position
    if y_coord == dim[0] - 1:
        y_end = y_coord
    else:
        y_end = y_coord + 1

    adjacent_tiles = list()
    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            if x == x_coord and y == y_coord:
                continue
            else:
                # print(x, y)
                adjacent_tiles.append(input_grid[y][x])
    
    return adjacent_tiles



def count_adjacent_occupied(input_grid, x_coord, y_coord):
    adjacent_states = get_adjacent_tiles(input_grid, x_coord, y_coord)
    return collections.Counter(adjacent_states)["#"]


# Gotta make a deep copy: just using copy makes a shallow copy (only the first elements of the list)
def one_iteration(input_grid):
    dim = dimensions(input_grid)
    output_grid = copy.deepcopy(input_grid)
    # Loop over the coordinates
    for y in range(dim[0]):
        for x in range(dim[1]):
            current_state = input_grid[y][x]
            if current_state == "L":
                if count_adjacent_occupied(input_grid, x, y) == 0:
                    output_grid[y][x] = "#"
            elif current_state == "#":
                if count_adjacent_occupied(input_grid, x, y) >= 4:
                    output_grid[y][x] = "L"
            else:
                continue
    return output_grid


def find_final_arrangement(input_grid):
    old_arrangement = list()
    new_arrangement = input_grid
    while old_arrangement != new_arrangement:
        old_arrangement = new_arrangement
        new_arrangement = one_iteration(old_arrangement)
    
    return new_arrangement

# Count occupied seats at the end of the iteration process
collections.Counter(''.join([''.join(x) for x in find_final_arrangement(example)]))["#"]

collections.Counter(''.join([''.join(x) for x in find_final_arrangement(input)]))["#"]


# Part 2

def see_seats_all_directions(input_grid, x_coord, y_coord):
    # Get dimensions
    dim = dimensions(input_grid)

    # Set up empty output
    seats_all_directions = list()
    # Loop over the possible directions we can move
    for x_dir in [-1, 0, 1]:
        for y_dir in [-1, 0, 1]:
        # If not moving, continue
            if x_dir == y_dir == 0:
                continue

            # Initialize checking location as 
            # One step from the seat we care about
            current_x = x_coord + x_dir
            current_y = y_coord + y_dir

            # Act as if we see an empty seat to start
            seat_seen = "."

            # If we're inbounds
            while current_x >= 0 and current_y >= 0 and current_x <= dim[1] -1 and current_y <= dim[0] - 1:
                if input_grid[current_y][current_x] not in ["L", "#"]:
                    # If it isn't an L or #, keep going
                    current_x += x_dir
                    current_y += y_dir
                else:
                    # Update the seat seen if we need to
                    seat_seen = input_grid[current_y][current_x]
                    break

            # Once out of the while loop, add the closest seen seat to our results for all directions
            seats_all_directions.append(seat_seen)


    return seats_all_directions



# Updating the iterations wit new rules
def one_iteration_pt2(input_grid):
    dim = dimensions(input_grid)
    output_grid = copy.deepcopy(input_grid)
    # Loop over the coordinates
    for y in range(dim[0]):
        for x in range(dim[1]):
            current_state = input_grid[y][x]
            if current_state == "L":
                seats_seen = see_seats_all_directions(input_grid, x, y)
                if collections.Counter(seats_seen)["#"] == 0:
                    output_grid[y][x] = "#"
            elif current_state == "#":
                seats_seen = see_seats_all_directions(input_grid, x, y)
                if collections.Counter(seats_seen)["#"] >= 5:
                    output_grid[y][x] = "L"
            else:
                continue
    return output_grid


def find_final_arrangement_pt2(input_grid):
    old_arrangement = list()
    new_arrangement = input_grid
    while old_arrangement != new_arrangement:
        old_arrangement = new_arrangement
        new_arrangement = one_iteration_pt2(old_arrangement)
    
    return new_arrangement

# Run it
collections.Counter(''.join([''.join(x) for x in find_final_arrangement_pt2(example)]))["#"]

collections.Counter(''.join([''.join(x) for x in find_final_arrangement_pt2(input)]))["#"]

