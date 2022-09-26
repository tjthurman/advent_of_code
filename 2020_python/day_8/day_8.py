

# Part 1
# Open instructions
with open("day_8/boot_instructions.txt") as f:
    instructions = f.read().splitlines()

# Initialize variables and set of completed instructions
instruc_row = 0
completed = []
accumulator = 0

while instruc_row not in completed: # as long as we're not repeating
    # Add current instruction row to the completed
    completed.append(instruc_row)
    # Figure out opperation and number
    current = instructions[instruc_row]
    operation = current[0:3]
    number = int(current[5:])
    if current[4] == "-":
        number = number * -1 
    # Do the operations
    if operation == "nop":
        instruc_row += 1
    if operation == "acc":
        accumulator += number
        instruc_row += 1
    if operation == "jmp":
        instruc_row += number


accumulator




# Part two
# Turn the above into a function
# Return success/fail, accumlator, and the instruction row
def run_program(instructions):
    
    # Initialize values
    instruc_row = 0
    completed = []
    accumulator = 0

    # Row value for exiting
    target = len(instructions)

    while instruc_row not in completed: # as long as we're not repeating

        if instruc_row == target: # if we're trying to process the last final row, we're done
            return([True, accumulator, instruc_row])

        # Add current instruction row to the completed
        completed.append(instruc_row)
        # Figure out opperation and number
        current = instructions[instruc_row]
        operation = current[0:3]
        number = int(current[5:])
        if current[4] == "-":
            number = number * -1 
        
        # Do the operations
        if operation == "nop":
            instruc_row += 1
        if operation == "acc":
            accumulator += number
            instruc_row += 1
        if operation == "jmp":
            instruc_row += number

    return([False, accumulator, instruc_row])



# Wrap the program running in a loop.
def debug_program(filename):

    with open(filename) as f:
        instructions = f.read().splitlines()
    
    # Find the jmp rows
    is_jmp = [line.split()[0] == "jmp" for line in instructions]
    jmp_rows = [i for i, x in enumerate(is_jmp) if x]

    # find the nop rows
    is_nop = [line.split()[0] == "nop" for line in instructions]
    nop_rows = [i for i, x in enumerate(is_nop) if x]


    # For each nop row
    for index in nop_rows:
        # print(index)

        # Make new instructions
        # new_instructions = instructions
        # SWEET JESUS. WENT DOWN A LONG, LONG DEBUG PATH
        # WHERE THIS DIDN"T WORK.
        # IN the above command, the two lists are still linked,
        # and changes to the new list are applied to the old one!!!
        # AGGGGH
        # must use below code, which creates a new unlinked list:
        new_instructions = instructions.copy()
        

        # replace the instruction
        new_instructions[index] = new_instructions[index].replace("nop", "jmp")
        
        # run 
        attempt = run_program(new_instructions)

        if attempt[0]:
            solution = "Switched command at line " + str(index)
            return([solution, attempt[1], attempt[2]])

    # Lazy double loop
    # For each jmp row
    for index in jmp_rows:
        # Make new instructions
        new_instructions = instructions.copy()
        # replace the instruction
        new_instructions[index] = new_instructions[index].replace("jmp", "nop")

        # print([instructions[index], new_instructions[index]])
        
        # run 
        attempt = run_program(new_instructions)

        if attempt[0]:
            solution = "Switched command at line " + str(index)
            return([solution, attempt[1], attempt[2]])
    

    return("Could not find solution")

debug_program("day_8/boot_instructions.txt")





    


    

