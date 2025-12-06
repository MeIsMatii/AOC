inputFile = "/home/mati/Documents/AOC/2025/Day4/testInput.txt"
def checkForPaperCurrentLine(line, index, exception):
    paperCounter2 = 0
    if index-1 != exception:
        if line[index-1] == '@':
            paperCounter2 += 1

    if index+1 != exception:
        if line[index+1] == '@':
            paperCounter2 += 1

    return paperCounter2


def checkForPaper(line, index, exception):
    paperCounter2 = 0

    if index-1 != exception:
        if line[index-1] == '@':
            paperCounter2 += 1

    if line[index] == '@':
        paperCounter2 += 1

    if index+1 != exception:
        if line[index+1] == '@':
            paperCounter2 += 1

    return paperCounter2

reachablePaper = 0
array = []
with open(inputFile, 'r') as file:
    for line in file:
        line = line.strip()
        array.append(list(line))

for i in range(len(array)):
    currentLine = array[i]
    if i > 0 and i < len(array)-1:
        nextLine = array[i+1]
        prevLine = array[i-1]
        for j in range(len(array[i])):
            paperCounter = 0
            if j > 0 and j < len(array[i])-1:
                if currentLine[j] == '@':

                    #check around the '@' # i know, reaallyyy efficient :D
                    paperCounter += checkForPaper(nextLine, j, 213123123132) #random wayy to big number
                    paperCounter += checkForPaper(prevLine, j, 213123123132) #random wayy to big number
                    paperCounter += checkForPaperCurrentLine(currentLine, j, 213123123132) #random wayy to big number
                    
                    if paperCounter < 4:
                        reachablePaper += 1
            elif j == 0:
                if currentLine[j] == '@':

                    #check around the '@' # i know, reaallyyy efficient :D
                    paperCounter += checkForPaper(nextLine, j, 0)
                    paperCounter += checkForPaper(prevLine, j, 0)
                    paperCounter += checkForPaperCurrentLine(currentLine, j, 0)
                    
                    if paperCounter < 4:
                        reachablePaper += 1
            
            else:
                if currentLine[j] == '@':

                    #check around the '@' # i know, reaallyyy efficient :D
                    paperCounter += checkForPaper(nextLine, j, len(array[i]))
                    paperCounter += checkForPaper(prevLine, j, len(array[i]))
                    paperCounter += checkForPaperCurrentLine(currentLine, j, len(array[i]))
                    
                    if paperCounter < 4:
                        reachablePaper += 1

print(reachablePaper)