import itertools
import math 

path = "python/aoc_2021/inputs/day04-1.txt"
with open(path) as f:
    input = [x.rstrip() for x in f]

# Separate draws and boards
draws = input[0].split(",")

boards = []
board_index = 0
current_board = []
for line in input[2:]:
    if line == "":
        boards.append(current_board)
        current_board = []
        board_index += 1
    else:
        current_board.append(line)
# And turn these into sequences
board_sequences = [" ".join(x).split() for x in boards]

# Generate all possible combinations of winning locations??
win_cols = []
for start in range(5):
    base = [False] * 5
    base[start] = True
    winner = list(itertools.chain(*list([base] * 5)))
    win_cols.append(winner)

win_rows = []
for start in range(0, 25, 5):
    winner = [False] * 25
    winner[start:(start+5)] = [True] * 5
    win_rows.append(winner)

win_diag_1 = []
for start in range(5):
    row = [False] * 5
    row[start] = True
    win_diag_1.append(row) 

win_diag_1 = [list(itertools.chain(*win_diag_1))]

win_diag_2 = []
for start in range(4, -1, -1):
    row = [False] * 5
    row[start] = True
    win_diag_2.append(row) 

win_diag_2 = [list(itertools.chain(*win_diag_2))]

winners = win_cols + win_rows + win_diag_1 + win_diag_2


# A function that checks the current state against all possible winners
def check_winner(state):
    for winner in winners:
        if sum([sum([x, y]) == 2 for x, y in zip(winner, state)]) == 5:
            return True
    return False

# A function to get a board score, at any state
def score_board(board_sequence, state, draw):
    unmarked = [int(not x) for x in state]
    board_sum = sum([math.prod([x, int(y)]) for x, y in zip(unmarked, board_sequence)])
    return int(draw) * board_sum


# A function that plays through the list of draws/plays
# and checks for winners as we go
def play_board(board_sequence, play_list):
    state = [False] * 25
    for index, play in enumerate(play_list):
        if play in board_sequence:
            state[board_sequence.index(play)] = True
        if check_winner(state):
            return (index, score_board(board_sequence, state, play))


all_plays = [play_board(x, draws) for x in board_sequences] 
turns_to_win = [x[0] for x in all_plays]
fastest_win = all_plays[turns_to_win.index(min(turns_to_win))]
fastest_win[1]

# Part 2
slowest_win = all_plays[turns_to_win.index(max(turns_to_win))]
slowest_win[1]
