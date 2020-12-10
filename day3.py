def advent3_1():
    with open("whatever.txt", "r") as file:
        arraythingy = [line.strip() for line in file.readlines()]
    #print(arraythingy)    
    pointer = 0
    counter = 0
    for x in arraythingy:
        if pointer < len(x):
            if x[pointer] == ".":
                pointer += 3
            else:
                pointer += 3
                counter += 1
        elif pointer >= len(x):
            pointer = pointer - len(x)
            if x[pointer] == ".":
                pointer += 3
            else:
                pointer += 3
                counter += 1
    return counter
    
def advent3_2():
    with open("whatever.txt", "r") as file:
        arraythingy = [line.strip() for line in file.readlines()]
    
    # make another array for every other line
    arrayby2 = []
    for evenline in arraythingy:
        if arraythingy.index(evenline) % 2 == 0:
            arrayby2.append(evenline)

    pointer = 0
    counter = 0
    slope = 1 # manually enter slope i guess
        
    
    for x in arrayby2:
        if pointer < len(x):
            if x[pointer] == ".":
                pointer += slope
            else:
                pointer += slope
                counter += 1
        elif pointer >= len(x):
            pointer = pointer - len(x)
            if x[pointer] == ".":
                pointer += slope
            else:
                pointer += slope
                counter += 1
    return counter
