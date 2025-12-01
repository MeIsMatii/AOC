import os
counter = 0 #counts how many zeroes there were
dial = 50 #dial begins at 50

with open('/home/mati/Documents/AOC/2025/Day1/puzzle1input.txt', 'r') as file:
    for line in file:
        line = line.strip() #it should be L/R, number 1-infinity

        direction = line[0] #first thing
        line = int(line[1:]) #2nd and onward

        if direction == "L":
            dial -= line
        else:
            dial += line

        if dial == 0:
            counter += 1

        if dial < 0:
            while dial <0:
                dial += 100
        elif dial > 99:
            while dial >0:
                dial -= 100
        print(counter, dial)


