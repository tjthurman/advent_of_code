
# Part 1
def find_row(row_string):
    rows = list(range(128))
    for x in list(row_string):
        if x == "F":
            rows = rows[:int(len(rows)/2)]
        if x == "B":
            rows = rows[int(len(rows)/2):]
    return int(rows[0])

find_row("FFFBBBF")
find_row("BBFFBBF")

def find_seat(seat_string):
    seats = list(range(8))
    for x in list(seat_string):
        if x == "L":
            seats = seats[:int(len(seats)/2)]
        if x == "R":
            seats = seats[int(len(seats)/2):]
    return int(seats[0])

# Get seat codes
with open("day_5/boarding_passes.txt") as f:
    barcodes = f.read().splitlines()

# Loop to get the seat_IDs
seat_IDs = []
for barcode in barcodes:
    row = find_row(barcode[:-3])
    seat = find_seat(barcode[-3:])
    seat_id = (row * 8)  + seat
    seat_IDs.append(seat_id)

max(seat_IDs)


# Part 2
occupied = set(seat_IDs)
possible = set(list(range(min(seat_IDs), max(seat_IDs))))
my_seat_ID = int(list(possible.difference(occupied))[0])
# There's the answer. But which row and seat am I?


for row in range(128):
    for seat in range(8):
        if (row * 8) + seat == my_seat_ID:
            print("My seat is in row {}, column {}".format(row, seat))
