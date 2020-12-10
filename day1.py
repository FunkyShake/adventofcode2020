def advent1_1():
    with open("intlist.txt", "r") as file:
        inties = {int(x) for x in file.readlines()}
        
    for num in inties:
        if (2020-num) in inties:
            return (num*(2020-num))
            
def advent1_2():
    with open("intlist.txt", "r") as file:
        inties = {int(x) for x in file.readlines()}
    
    for num in inties:
        othernums = {x for x in inties if x != num}
        for second in othernums:
            if (2020-num-second) in othernums:
                third = (2020-num-second)
                return (num * second * third)
