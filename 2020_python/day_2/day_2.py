# Password debugging

import re


with open("day_2/passwords.txt") as f:
    lines = f.read().splitlines()


# Part 1:
# Define a function that checks the validity of the password according to the given rules:
# the character must appear a certain numner of times in the password
def check_pword_valid(min, max, character, password):
    matches = len(re.findall(character,  password))
    if min <= matches <= max:
        return True
    else:
        return False


valid_passwords = 0
for line in lines:
    entry = re.split('-| |: |, ', line)
    valid = check_pword_valid(min = int(entry[0]), 
                          max = int(entry[1]),  
                          character = entry[2],
                          password = entry[3])
    if valid:
        valid_passwords += 1
    
## Part 2
# New rules, new function
def check_pword_valid2(pos1, pos2, character, password):
    validity = [password[pos1 -1] == character, password[pos2 -1] == character]
    if sum(validity) == 1:
        return True
    else:
        return False

# Loop over entries with our function
valid_passwords2 = 0
for line in lines:
    entry = re.split('-| |: |, ', line)
    valid = check_pword_valid2(pos1 = int(entry[0]), 
                          pos2 = int(entry[1]),  
                          character = entry[2],
                          password = entry[3])
    if valid:
        valid_passwords2 += 1