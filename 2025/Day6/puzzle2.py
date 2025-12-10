inputFile = '2025/Day6/testInput.txt'
temp = ''
grid = []
with open(inputFile, 'r') as file:
    for line in file:
        line = line.strip().split(' ')

        
        newList = []
        for i in range(len(line)):
            if line[i] != ' ' and line[i] != '':
                newList.append(line[i])

        grid.append(newList)
for i in range(len(grid)):
    print(str(grid[i]))

length = len(grid[0])
totalSum = 0


for i in range(length):
    numbers = []
    currentSum = 0
    for j in range(len(grid)):
        if j != len(grid) -1:
            numbers.append(grid[j][i])
        else:
            operator = grid[j][i]
    for j in range(len(numbers)):
        if operator == '+':
            currentSum += int(numbers[j])
        elif operator == '*':
            if currentSum == 0:
                currentSum = 1
            currentSum *= int(numbers[j])
    totalSum += currentSum

print(totalSum)