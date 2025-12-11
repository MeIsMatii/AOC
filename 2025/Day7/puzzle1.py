inputFile = '2025/Day7/testInput.txt'
grid = []
with open(inputFile, 'r') as file:
    for line in file:
        file = list(line.strip())
        grid.append(file)

for i in range(len(grid[0])):
    if grid[0][i] == 'S':
        shipPosX = (i)
    
grid[1][shipPosX] = '|'


beams = 1
while beams > 0:
    beams = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if str(grid[i][j]) != '|':
                continue
        
            beams +=1
            beamPos = (i,j)

            for i in range(len(grid)):
                grid[i][j] = '.'
                if i == len(grid) - 1:
                    beams -= 1
                    break
                if str(grid[i+1][j]) != '^':
                    grid[i+1][j] = '|'
                else:
                    if j - 1 >= 0:
                        grid[i+1][j-1] = '|'
                    if j + 1 < len(grid[i]):
                        grid[i+1][j+1] = '|'
                    
# beams = [shipPosX]
# for i in range(len(grid)):
#     if str(grid[i][shipPosX]) != '^':
#         grid[i][shipPosX] = '|'
#         for j in range(len(beams)):
#             if beams[j][1] == grid[i - 1][shipPosX]:
#                 beams[j][1] = (grid[i],shipPosX)
#                 break
#     else:
#         beams.remove((i,shipPosX))
#         beams.append((i,shipPosX - 1))
#         beams.append((i,shipPosX + 1)) #split beam    

