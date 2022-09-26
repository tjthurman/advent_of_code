# Passports



import re

def process_batch(filename):
    # Read in file as lines, keeping newlinws
    with open(filename) as f:
        lines = f.readlines()
    # Set up results
    passports = list()
    # set up a singel password
    one_passport = str()

    for line in lines:
        if line != '\n': # if its not a spacer
            one_passport += line # add to the single passport
        else: # if a spacer
            passports.append(one_passport) # write out single passport
            one_passport = str() # reset

    out = [x.replace('\n', ' ') for x in passports]

    return out


def check_passport_valid(passport):
    split_passport = passport.split()
    if len(split_passport) == 8:
        return True
    elif len(split_passport) == 7:
        if re.search(pattern = "cid:", string = passport):
            return False
        else:
            return True
    else:
        return False


passports = process_batch("day_4/passports.txt")

sum([check_passport_valid(x) for x in passports])

# Part 2
# Some real validity checks

# i think my strategy will be to assemble each passport into a dict, 
# then write checks to test each element.

# Passport string (from procees batch) to dict
def passport_string_to_dict(passport_string):
    return dict(zip(re.split(":| ", passport_string)[::2], re.split(":| ", passport_string)[1::2]))

# There might be some sort of multiple-dispatch or OO
# approach or something I could take here. 
# But I don;t know how to do any of that shit, so
# complicated if/else statments it is. 
def check_field(field_name, field_value):
    if field_name == "byr":
        validity = 1920 <= int(field_value) <= 2002
    elif field_name == "iyr":
        validity = 2010 <= int(field_value) <= 2020
    elif field_name == "eyr":
        validity = 2020 <= int(field_value) <= 2030
    elif field_name == "hgt":
        units = field_value[-2:]
        height = int(field_value[:-2])
        if units == "cm":
            validity = 150 <= height <= 193
        elif units == "in":
            validity = 59 <= height <= 76
        else:
            validity = False
    elif field_name == "hcl":
        if re.match(r'^#[0-9,a-f]{6}', field_value):
            validity = True
        else:
            validity = False
    elif field_name == "ecl":
        good_ecl = "amb blu brn gry grn hzl oth"
        if re.search(field_value, good_ecl):
            validity = True
        else:
            validity = False
    elif field_name == "pid":
        if re.match(r'^[0-9]{9}$', field_value):
            validity = True
        else:
            validity = False
    elif field_name == "cid":
        return True
    else:
        validity = False
    return validity

# A function that checks all fields of a single passport
def check_passport_valid2(passport_string):
    fields_to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    pass_dict = passport_string_to_dict(passport_string)
    if len(pass_dict) < 7: # Not enough fields, false
        return False
    if len(pass_dict) == 7:
        if "cid" in [*pass_dict]:
            return False
    for field in fields_to_check:
        if not check_field(field, pass_dict[field]):
            return False
    return True



sum([check_passport_valid2(x) for x in passports])



