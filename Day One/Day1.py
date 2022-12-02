with open('calories.txt') as f:
    sweeps = [line.rstrip().split("\n\n") for line in f]  #  This variable name is from day one of 2021

entry =[]
entries = []
for x in sweeps:  #  I KNOW theres a way to do this in the with loop and I think i've done it before.
    if x[0] != "":
        entry.append(int(x[0]))
    else:
        entries.append(entry)
        entry = []

totals = []
for x in entries:
    current = sum(x)
    totals.append(current)

totals.sort()
totals.reverse()
print("Part One: ", max(totals))  
print("Part Two: ", totals[0]+totals[1]+totals[2])