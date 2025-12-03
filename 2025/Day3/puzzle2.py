inputFile = "/workspaces/AOC/2025/Day3/puzzleInput.txt"

totalSum = 0
with open(inputFile, 'r') as file:
    for line in file:
        number1 = 0
        number2 = 0
        number3 = 0
        number4 = 0
        number5 = 0
        number6 = 0
        number7 = 0
        number8 = 0
        number9 = 0
        number10 = 0
        number11 = 0
        number12 = 0
        numberIndex = 0
        line = line.strip() #it should be a really long string
        for number in range(1,12):
        
            for i in range(len(line)):
                currentJoltage = int(line[i])
                if currentJoltage > number1 and i < len(line) -1:
                    number1+ i= currentJoltage
                    numberIndex = i
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
            if number1 < currentJoltage and i < len(line) -1:
                number1 = currentJoltage
                numberIndex = i

        for i in range(numberIndex + 1,len(line)):
            currentJoltage = int(line[i])
            if number2 < currentJoltage and i < len(line) -1:
                number2 = currentJoltage    
                numberIndex = i
        
        for i in range(numberIndex + 1, len(line)):
            currentJoltage = int(line[i])
            if currentJoltage > number3 and i < len(line) -1:
                number3+ i= currentJoltage
                numberIndex = i    

        for i in range(numberIndex + 1, len(line)):
            currentJoltage = int(line[i])
            if currentJoltage > number4 and i < len(line) -1:
                number4+ i= currentJoltage
                numberIndex = i    
    
        for i in range(numberIndex+1, len(line)):
            currentJoltage = int(line[i])
            if currentJoltage > number5 and i < len(line) -1:
                number5+ i= currentJoltage
                numberIndex = i    
    
    
        
        totalSum += int(str(number1) + str(number2) + str(number3) + str(number4) + str(number5) + str(number6) + str(number7) + str(number8) + str(number9) + str(number10) + str(number11) + str(number12))
        print(totalSum)
print(number1,number2)