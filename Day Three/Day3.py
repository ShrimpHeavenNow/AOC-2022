with open('calories.txt') as f:
    sweeps = [line.rstrip().split("\n\n") for line in f]  #  This variable name is from day one of 2021