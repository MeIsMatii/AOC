inputFile = "/home/mati/Documents/AOC/2025/Day4/testInput.txt"

def do_something(grid):
    reachablePaper = 0
    newGrid = list(grid)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            paperCounter = 0
            if grid[y][x] != '@':
                continue
            for ny in range(y-1, y+2):
                for nx in range(x-1, x+2):
                    if nx == x and ny == y:
                        continue
                    if nx >= 0 and nx < len(grid[y]) and ny >= 0 and ny < len(grid): #if its not "out of bounds"
                        if grid[ny][nx] == '@':
                            paperCounter += 1
            if paperCounter < 4:
                reachablePaper += 1
                newGrid[y][x] = '.'
    grid = newGrid
    return(reachablePaper)
                

reachablePaper = 0
grid = []
with open(inputFile, 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

check = False
while check == False:
    temp = reachablePaper

    reachablePaper += do_something(grid)

    if temp == reachablePaper:
        check = True
print(reachablePaper)