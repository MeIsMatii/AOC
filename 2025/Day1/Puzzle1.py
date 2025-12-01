import os
counter = 0 #counts how many zeroes there were
dial = 50 #dial begins at 50

with open('/home/mati/Documents/AOC/2025/Day1/puzzle1input.txt', 'r') as file:
    for line in file:
        line = line.strip() #it should be L/R, number 1-infinity

        direction = line[0] #first thing
        rotations = int(line[1:]) #2nd and onward

        if direction == "L":
            dial -= rotations
        else:
            dial += rotations

        

        dial = dial % 100
        

        if dial == 0:
            counter += 1
        if dial < 0 or dial > 100:
            print("somethings wrong")
            break

print(counter)