def advent4_1():
    with open ("pp.txt", "r") as file:
        ppls = [x for x in file.read().split("\n\n")]
    valid = 0
    for x in ppls:
        x = x.replace("\n", " ")
        if len(x.split(" ")) == 8:
            valid += 1
        elif len(x.split(" ")) == 7 and "cid:" not in x:
            valid += 1
        else:
            pass
    print(valid)
