inputFile = '2025/Day7/puzzleInput.txt'
grid = []
with open(inputFile, 'r') as file:
    for line in file:
        file = list(line.strip())
        grid.append(file)

for i in range(len(grid[0])):
    if grid[0][i] == 'S':
        grid[1][i] = '|'
        break

splits = 0

# for i in range(len(grid)):
#     print(''.join(grid[i]))

for i in range(1,len(grid) -1 ):
    for j in range(len(grid[i])):

        if str(grid[i][j]) != '|':
            continue

        if i == len(grid) - 1:
            break
            
        if str(grid[i+1][j]) != '^':
            grid[i+1][j] = '|'
        
        else:
            splits += 1
            if i - 1 >= 0:
                grid[i+1][j-1] = '|'
            if i + 1 < len(grid[i]):
                grid[i+1][j+1] = '|'

print(splits)   
# for i in range(len(grid)):
#     print(''.join(grid[i]))