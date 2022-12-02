with open('farts.txt') as f:
    sweeps = [line.rstrip().split("\n") for line in f]  #  This variable name is from day one of 2021

score = 0
for x in sweeps:  # I do this better in part two, but not by much.
    if x[0][0] == 'A' and x[0][2] == 'X':
        score += 3
    if x[0][0] == 'A' and x[0][2] == 'Y':
        score +=6
    if x[0][0] == 'B' and x[0][2] == 'Y':
        score += 3
    if x[0][0] == 'B' and x[0][2] == 'Z':
        score += 6
    if x[0][0] == 'C' and x[0][2] == 'X':
        score += 6
    if x[0][0] == 'C' and x[0][2] == 'Z':
        score +=3
    if x[0][2] == "X":
        score +=1
    if x[0][2] == "Y":
        score +=2
    if x[0][2] == "Z":
        score +=3

print("Part One: ", score)

#  x is lose, y is draw, z is win
score =0
for x in sweeps:
    for y in x:
        if y[0] == "A":
            if y[2] == "X":
                score += 3
            if y[2] == "Y":
                score += 4
            if y[2] == "Z":
                score += 8
        if y[0] == "B":
            if y[2] == "X":
                score += 1
            if y[2] == "Y":
                score += 5
            if y[2] == "Z":
                score += 9
        if y[0] == "C":
            if y[2] == "X":
                score += 2
            if y[2] == "Y":
                score += 6
            if y[2] == "Z":
                score += 7
print("Part Two: ", score)

