inputFile = '2025/Day7/testInput.txt'
grid = []
with open(inputFile, 'r') as file:
    for line in file:
        file = list(line.strip())
        grid.append(file)


for i in range(len(grid[0])):
    if grid[0][i] == 'S':
        shipPosX = (i)
beams = [shipPosX]
for i in range(len(grid)):
    if str(grid[i][shipPosX]) != '^':
        grid[i][shipPosX] = '|'
        for j in range(len(beams)):
            if beams[j][1] == grid[i - 1][shipPosX]:
                beams[j][1] = (grid[i],shipPosX)
                break
    else:
        beams.remove((i,shipPosX))
        beams.append((i,shipPosX - 1))
        beams.append((i,shipPosX + 1)) #split beam    

