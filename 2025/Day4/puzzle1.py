inputFile = "/workspaces/AOC/2025/Day4/testInput.txt"
lineCounter = 0
currentLineCounter = -1
reachablePaper = 0
with open(inputFile, 'r') as file:
    print(file)
    for currentLine in file:
        currentLineCounter +=1
        previous = True
        next = True
        currentLine = currentLine.strip()
        nextLine = file[currentLineCounter +1].strip()

        if currentLineCounter == file:
            next = False
        elif currentLineCounter == 0:
            previous = False
        for i in range(len(currentLine)):
            paperCounter = 0
            if i > 0 and i < len(currentLine) -1:
                
                if currentLine[i] == "@":
                    if currentLine[i-1] == "@":
                        paperCounter += 1
                    if currentLine[i+1] == "@":
                        paperCounter += 1

                    if previous == True:
                        if previousLine[i] == "@":
                            paperCounter += 1
                        if previousLine[i-1] == "@":
                            paperCounter += 1
                        if previousLine[i+1] == "@":
                            paperCounter += 1

                    if next == True:
                        if nextLine[i] == "@":
                            paperCounter += 1
                        if nextLine[i-1] == "@":
                            paperCounter += 1
                        if nextLine[i+1] == "@":
                            paperCounter += 1

                    if paperCounter < 4:
                        reachablePaper += 1


            previousLine = currentLine
print(reachablePaper)