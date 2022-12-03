with open('Day3.txt') as f:
    sweeps = [line.rstrip().split("\n") for line in f]  #  This variable name is from day one of 2021

scores = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26, "A" : 27, "B" : 28, "C" : 29, "D" : 30, "E" : 31, "F" : 32, "G" : 33, "H" : 34, "I" : 35, "J" : 36, "K" : 37, "L" : 38, "M" : 39, "N" : 40, "O" : 41, "P" : 42, "Q" : 43, "R" : 44, "S" : 45, "T" : 46, "U" : 47, "V" : 48, "W" : 49, "X" : 50, "Y" : 51, "Z" : 52, }
sackOne = []
sackTwo = []

for x in sweeps:
    for y in x:
        slice = int(len(y)/2)
        sackOne.append(y[:slice])
        sackTwo.append(y[slice:])

common = []
for x in range(0,len(sackOne)):
    for y in sackOne[x]:
        if y in sackTwo[x]:
            common.append(y)
            break

answer = 0
for x in common:
    answer += scores[x]

print("Part One: ", answer)

groups = []
i = 0
beef = 0
while i < len(sweeps)/3:
    groups.append([])
    for q in range(0,3):
        try:
            groups[i].append(sweeps[beef][0])
        except:
            break
        beef += 1
    i += 1

common = []
for x in range(0,len(groups)):
    for y in groups[x][0]:
        if y in groups[x][1] and y in groups[x][2]:
            common.append(y)
            break

answer = 0
for x in common:
    answer += scores[x]

print("Part Two: ", answer)