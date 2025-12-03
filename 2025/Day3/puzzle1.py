number1 = 0
number2 = 0
number1index = 0
with open('puzzleInput.txt', 'r') as file:
    for line in file:
        line = line.strip() #it should be a really long string
        
        for i in range(len(line)):
            currentJoltage = line[i]
            if currentJoltage < number1 and i < len(line) -1:
                number1 = currentJoltage
                number1index = i



with open('puzzleInput.txt', 'r') as file:
    for line in file:
        line = line.strip()
        for i in range(number1index, len(line)):
            if currentJoltage < number2:
                number2 = currentJoltage