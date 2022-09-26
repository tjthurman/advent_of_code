
# part 1
# Open the files as a long string, split each group by splitting at double newlines
with open("day_6/answers.txt") as f:
        lines = str(f.read())
        groups = lines.split(sep = "\n\n")


# For each group, replace newlines and take set to find unique questions
# answered yes
all_yes = 0
for group in groups:
    group_yes = len(set(list(group.replace("\n", ""))))
    all_yes += group_yes

all_yes

# Part 2
# From any yes to every yes per question
# Old way that didn't work
# Make groups as above. Then:
all_qs_yes = list()
for group in groups:
    inds = len(group.split(sep = "\n"))
    group_string = group.replace("\n", "")
    chr_counts = [group_string.count(i) == inds for i in set(group_string)]
    all_qs_yes.append(sum(chr_counts))
sum(all_qs_yes)  #3278, too small. 

# Instead will make groups a new way (list of lists this time):
with open("day_6/answers.txt") as f:
    lines = str(f.read())

import string # to get the set of lowercase letters

# This time, do lists of lists
groups2 = lines.split(sep = "\n\n")
groups2 = [line.split() for line in groups]


all_qs_yes2 = list()
for group in groups2:
    all_yes = ["".join(group).count(letter) == len(group) for letter in string.ascii_lowercase]
    all_qs_yes2.append(sum(all_yes))
# This one worked.
sum(all_qs_yes2) # 3299

# Why are they different?
len(all_qs_yes)
len(all_qs_yes2)
# Same length

all_qs_yes == all_qs_yes2

[ x == y for (x,y) in zip(all_qs_yes, all_qs_yes2)].index(False) # The last element is the problem

groups[463]
groups2[463]

# Testing my original code on this last group
group = groups[463]
inds = len(group.split(sep = "\n")) # Here's the problem. That trailing endline in the
# last group didn't get deleted in the original processing, so it split to 5
# individuals where there are only 4, with the last individual empty.
# That meant none of the questions were answered, so my original one was too low. 
group_string = group.replace("\n", "")
chr_counts = [group_string.count(i) == inds for i in set(group_string)]
all_qs_yes.append(sum(chr_counts))

# Actually, this was all my own fault.
# If I hadn't specified the separator in split, my original technique worked as well:
all_qs_yes = list()
for group in groups:
    inds = len(group.split())
    group_string = group.replace("\n", "")
    chr_counts = [group_string.count(i) == inds for i in set(group_string)]
    all_qs_yes.append(sum(chr_counts))
sum(all_qs_yes)  #3278, too small. 

# To be honest, I don't totally understand that: the defauly separator is
# any whitespace, of which \n is a subset. I'm not sure why it doesn't remove all trailing
# whitespace when you specify the separator. 