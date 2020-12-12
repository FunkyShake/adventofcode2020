from itertools import combinations

with open('day9.txt') as f:
    day9ls = [int(x) for x in f.readlines()]
preindex = 0
postindex = 25
for numbers in day9ls:
    values = [sum(x) for x in combinations(day9ls[preindex:postindex], 2)]
    if day9ls[postindex] in values:
        preindex += 1
        postindex += 1
    else:
        print(day9ls[postindex])
        break
        
# part 2
