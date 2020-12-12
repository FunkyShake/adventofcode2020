with open('day10.txt') as f:
    day10ls = [int(x) for x in f.readlines()]

day10ls.sort(reverse=True)
gap1 = 0
gap3 = 1
for number in range(len(day10ls)):
    if day10ls[number] >= 2:
        if day10ls[number] - day10ls[number + 1] == 1:
            gap1 += 1
        else:
            gap3 += 1
    if day10ls[number] == 1:
        gap1 += 1
        break
print(gap3 *gap1)

# part 2
