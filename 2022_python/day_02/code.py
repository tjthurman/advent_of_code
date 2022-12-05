
path = "2022_python/day_02/input.txt"
with open(path) as f:
       lines = [x.rstrip() for x in f]

moves = [tuple(x.split()) for x in lines]



# Set up the rules
op_key = {
    "A" :"rock",
    "B" :"paper",
    "C" : "scissors"
}

my_key = {
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors"
}

game_key = {
  "rockrock" : 3,
  "rockscissors" : 0,
  "rockpaper" : 6,
  "paperpaper": 3,
  "paperscissors" : 6,
  "paperrock" : 0,
  "scissorsscissors" : 3,
  "scissorspaper" : 0,
  "scissorsrock" : 6
}

play_key = {
    "rock" : 1,
    "paper" : 2,
    "scissors" : 3
}

def rps(opponent, me):
    return game_key[op_key[opponent] + my_key[me]] + play_key[my_key[me]]

sum([rps(opponent, me) for (opponent, me) in moves])

# Part 2
# Rules have changed
possible_games = [
    ["rock", "rock", "draw"],
    ["rock", "scissors", "lose"],
    ["rock", "paper", "win"],
    ["paper", "paper", "draw"],
    ["paper", "scissors", "win"],
    ["paper", "rock", "lose"],
    ["scissors", "scissors", "draw"],
    ["scissors", "paper", "lose"],
    ["scissors", "rock", "win"]
]

goal_key = {
    "X" : "lose",
    "Y" : "draw",
    "Z" : "win"
}
