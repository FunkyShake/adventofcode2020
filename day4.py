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

# i did not write this next part, woe is me
# I think you need an extra new line at the end of your file
# part 2
REGEX = [
    r"byr:(?:19[2-9]\d|200[0-2])\b",
    r"iyr:20(?:1\d|20)\b",
    r"eyr:20(?:2\d|30)\b",
    r"hgt:(?:1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)\b",
    r"hcl:#[0-9a-f]{6}\b",
    r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b",
    r"pid:\d{9}\b",
]
with open("pp.txt") as f:
    lines = f.read()[:-1].split("\n\n")
    print(sum(all(re.search(x, s) for x in REGEX) for s in lines))
