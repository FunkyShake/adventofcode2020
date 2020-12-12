with open('day8.txt') as f:
    day8ls = [x.strip().split(' ') for x in f.readlines()]

ruleindices = set()
uniquerules = True
ruleindex = 0
accumulator = 0

while uniquerules == True:
    if ruleindex not in ruleindices:
        print(ruleindex)
        if day8ls[ruleindex][0] == 'nop':
            ruleindices.add(ruleindex)
            ruleindex += 1
            
        if day8ls[ruleindex][0] == 'acc':
            ruleindices.add(ruleindex)
            if '+' in day8ls[ruleindex][1]:
                accumulator += int(day8ls[ruleindex][1][1:])
                ruleindex += 1
            else:
                accumulator -= int(day8ls[ruleindex][1][1:])
                ruleindex += 1
                
        if day8ls[ruleindex][0] == 'jmp':
            ruleindices.add(ruleindex)
            if '+' in day8ls[ruleindex][1]:
                ruleindex += int(day8ls[ruleindex][1][1:])
            else:
                ruleindex -= int(day8ls[ruleindex][1][1:])
    else:
        uniquerules = False
        print(accumulator)

# part 2
