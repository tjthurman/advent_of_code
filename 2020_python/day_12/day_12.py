# Part 1

with open("day_12/example.txt") as f:
    lines =  f.read().splitlines()
    example = [[x[:1], x[1:]] for x in lines]
 

with open("day_12/input.txt") as f:
    lines =  f.read().splitlines()
    input = [[x[:1], x[1:]] for x in lines]


start_x = 0
start_y = 0


# Set up a nested dictionary to conver facings and directions
# to cardinal directions
facing_to_dir_dict={'0':{'F':"E", "R":"W"}, '90':{'F':"N", "R":"S"}, '180':{'F':"W", "R":"E"}, '270':{'F':"S", "R":"N"}}

def move_ship(current_x, current_y, facing, command, number):
    out_x = current_x
    out_y = current_y
    out_face = facing

    # Simple Cardinal directions
    if command == "E":
        out_x += int(number)
    if command == "W":
        out_x -= int(number)
    if command == "N":
        out_y += int(number)
    if command == "S":
        out_y -= int(number)

    # Simple rotation
    if command == "R":
        out_face -= int(number)
    if command == "L":
        out_face += int(number)
        
    # keep everything on positive 360 degrees
    if out_face < 0:
        out_face += 360
    if out_face >= 360:
        out_face -= 360

    # Forward and Back:
    # Convert to a regular command and go recursive
    if command == "F":
        command = facing_to_dir_dict[str(facing)][command]
        z = move_ship(out_x, out_y, out_face, command, number)
        out_x = z[0]
        out_y = z[1]
        out_face = z[2]

    return [out_x, out_y, out_face]

move_ship(10, 12, 90, "E", 30)

def full_journey(directions_list):
    x_pos = 0
    y_pos = 0
    facing = 0

    for x in directions_list:
        print(x_pos, y_pos, facing)
        new = move_ship(x_pos, y_pos, facing, x[0], x[1])
        x_pos = new[0]
        y_pos = new[1]
        facing = new[2]
    
    return abs(x_pos) + abs(y_pos)

full_journey(example)
full_journey(input)

# Part 2
import numpy as np

# Use some linear algebra to do the rotation of the waypoint
def rotate_waypoint(waypoint_x, waypoint_y, command, degrees):
        theta = np.radians(degrees)
        if command == "L":
            theta *= -1
        c, s = np.cos(theta), np.sin(theta) 
        rot_matrix = np.array(((c, -s), (s,c)))

        rotated = np.array([waypoint_x, waypoint_y]).dot(rot_matrix)

        return [int(np.rint(x)) for x in rotated]

def move_ship_and_waypoint(ship_x, ship_y, waypoint_x, waypoint_y, command, number):
    # Set up outputs
    out_ship_x = ship_x
    out_ship_y = ship_y
    out_waypoint_x = waypoint_x
    out_waypoint_y = waypoint_y

    # Simple Cardinal directions
    if command == "E":
        out_waypoint_x += int(number)
    if command == "W":
        out_waypoint_x -= int(number)
    if command == "N":
        out_waypoint_y += int(number)
    if command == "S":
        out_waypoint_y -= int(number)

    # Waypoint rotation
    if command in ["R", "L"]:
        rotated = rotate_waypoint(out_waypoint_x, out_waypoint_y, command, number) 
        out_waypoint_x = rotated[0]
        out_waypoint_y = rotated[1]
        
    # Forward:
    if command == "F":
        out_ship_x += number * waypoint_x
        out_ship_y += number * waypoint_y     
    
    return [out_ship_x, out_ship_y, out_waypoint_x, out_waypoint_y]


def full_journey_pt2(directions_list):
    x_pos = 0
    y_pos = 0
    x_way = 10
    y_way = 1

    for x in directions_list:
        print(x_pos, y_pos, x_way, y_way)
        new = move_ship_and_waypoint(x_pos, y_pos, x_way, y_way, x[0], int(x[1]))
        x_pos = new[0]
        y_pos = new[1]
        x_way = new[2]
        y_way = new[3]
    
    return abs(x_pos) + abs(y_pos)
    
full_journey_pt2(example)
full_journey_pt2(input)
