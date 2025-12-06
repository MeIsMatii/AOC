inputFile = "/home/mati/Documents/AOC/2025/Day4/testInput.txt"

def do_something(array):
    reachablePaper = 0
    newArray = list(array)

    for y in range(len(array)):
        for x in range(len(array[y])):
            paperCounter = 0
            if array[y][x] != '@':
                continue
            for ny in range(y-1, y+2):
                for nx in range(x-1, x+2):
                    if nx == x and ny == y:
                        continue
                    if nx >= 0 and nx < len(array[y]) and ny >= 0 and ny < len(array): #if its not "out of bounds"
                        if array[ny][nx] == '@':
                            paperCounter += 1
            if paperCounter < 4:
                reachablePaper += 1
                newArray[y][x] = '.'
    array = newArray
    return(reachablePaper)
                

reachablePaper = 0
array = []
with open(inputFile, 'r') as file:
    for line in file:
        line = line.strip()
        array.append(list(line))

check = False
while check == False:
    temp = reachablePaper

    reachablePaper += do_something(array)
    
    if temp == reachablePaper:
        check = True
print(reachablePaper)