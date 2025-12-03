inputFile = "/workspaces/AOC/2025/Day3/testInput.txt"


totalSum = 0
with open(inputFile, 'r') as file:
    for line in file:
        joltages = []

        line = line.strip() #it should be a really long string
        print(line)

        for i in range(12):
            numberIndex = 0
            highestJoltage = 0
            x = 0
            k = 11 - i

            if i > 0:
                x = 1

            for j in range(numberIndex +x, len(line)):
                currentJoltage = int(line[j])
                if j > len(line) -k:
                    break
                if highestJoltage < currentJoltage: 
                    if j < len(line):
                        highestJoltage = currentJoltage
                        numberIndex = j
            joltages.append(highestJoltage)
            k-=1
                
            print(joltages)
            print(line)
        for i in range(len(joltages)):
            totalSum += joltages[i] * (10 ** (11 - i)) #to place the digits in the correct position (first is 10**11, second 10**10 and last 10*0)
        #totalSum += int(str(highestJoltage) + str(number2) + str(number3) + str(number4) + str(number5) + str(number6) + str(number7) + str(number8) + str(number9) + str(number10) + str(number11) + str(number12))

#print(totalSum)
#print(number1,number2)