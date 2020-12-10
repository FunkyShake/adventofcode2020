import re

def advent2_1():
    with open("pw.txt", "r") as file:
        testy = [x.strip() for x in file.readlines()]
    counter = 0
    for x in testy:
        x = re.split('-|:| ', x)
        letter = x[2]
        if x[4].count(letter) in range(int(x[0]), int(x[1])+1):
            counter += 1
    return counter

def advent2_2():
    with open("pw.txt", "r") as file:
        testypw = [x.strip() for x in file.readlines()]
    counter = 0
    for x in testypw:
        x = re.split('-|:| ', x)
        ind1, ind2, letter, pw = int(x[0]), int(x[1]), x[2], x[4]
        
        if pw[(ind1)-1] == letter and pw [(ind2)-1] == letter:
            pass
        elif pw[(ind1)-1] == letter and pw [(ind2)-1] != letter:
            counter += 1
        elif pw[(ind1)-1] != letter and pw [(ind2)-1] == letter:
            counter += 1
        else:
            pass
    return counter
