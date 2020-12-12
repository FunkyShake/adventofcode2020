with open('day5.txt', 'r') as f: 
    day5ls = [x.strip() for x in f.readlines()]
    
def halve(code, rows):
    for letter in code:
        if letter in ('B', 'R'):
            rows = rows[len(rows)//2:]
        if letter in ('F', 'L'):
            rows = rows[:len(rows)//2]
            
    return rows
def calcalater(code):
    rows = list(range(128))
    seats = list(range(8))
    rowcode = code[:7]
    seatcode = code[7:]
             
    rows = halve(rowcode, rows)
    seats = halve(seatcode, seats)
    return rows[0], seats[0]

def answer(rows, seats):
    return rows * 8 + seats
def sandwich(codes):
    calcs = [answerr(*calcalater(code)) for code in codes]
    return max(calcs)

# part 2
def cream(codes):
    calcs = [answerr(*calcalater(code)) for code in codes]
    return calcs

print(sandwich(day5ls))
for x in range(84,901):
    if x not in cream(day5ls):
        print(x)
