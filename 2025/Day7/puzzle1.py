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

splits = 0
beams = 1

for i in range(len(grid)):
    print(''.join(grid[i]))

for i in range(1,len(grid) -1 ):
    for j in range(len(grid[i])):
        if str(grid[i][j]) != '|':
            continue

        for k in range(len(grid)):
            if k == len(grid) - 1:
                break
            if str(grid[i+1][j]) != '^':
                grid[i+1][j] = '|'
            else:
                splits += 1
                if k - 1 >= 0:
                    beams += 1
                    grid[i+1][j-1] = '|'
                if k + 1 < len(grid[i]):
                    beams += 1
                    grid[i+1][j+1] = '|'
                for x in range(len(grid)):
                    print(''.join(grid[x]))
                print('------------')

print(splits)   
for i in range(len(grid)):
    print(''.join(grid[i]))
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

