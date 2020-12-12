def advent6_1():
    with open('day6.txt', 'r') as f:
        day6ls = [set(x) for x in f.read().split('\n\n')]
    
    total = 0
    for item in day6ls:
        if '\n' in item:
            total += (len(item) - 1)
        else:
            total += len(item)
    return total
    
# part 2

with open('day6.txt', 'r') as f:
    day6ls = [x.split() for x in f.read().split('\n\n')]
print('part 2:', sum(len([letter for letter in day6[0] if all(letter in x for x in day6)]) for day6 in day6ls))
