inputFile = "/workspaces/AOC/2025/Day3/puzzleInput.txt"

totalSum = 0
with open(inputFile, 'r') as file:
    for line in file:
        number1 = 0
        number2 = 0
        number1index = 0
        line = line.strip() #it should be a really long string
        
        for i in range(len(line)):
            currentJoltage = int(line[i])
            if currentJoltage > number1 and i < len(line) -1:
                number1 = currentJoltage
                number1index = i
        for i in range(number1index + 1,len(line)):
            currentJoltage = int(line[i])
            if number2 < currentJoltage:
                number2 = currentJoltage            
        print(number1, number2)
        totalSum += 10*number1 + number2 
        print(totalSum)
print(number1,number2)