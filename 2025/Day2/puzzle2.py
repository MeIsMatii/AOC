
def checkRepeating(id):
    idString = str(id)
    # Check for all possible lengths of repeating patterns
    for length in range(1, len(idString) // 2 + 1):
        # Repeat the substring and check if it matches the original string
        if (idString[:length] * (len(idString) // length)) == idString:
            return True
    return False

total_sum = 0   
with open('/home/mati/Documents/AOC/2025/Day2/puzzleInput.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(",")
         
    for i in range(len(line)):
        

        idRange = line[i].split("-") # idRange now is a list with fromId (at 0) and toId (at 1)
        fromId = int(idRange[0])
        toId = int(idRange[1])

        while fromId <= toId: #banned stuff:
            if str(fromId)[0] == "0":
                total_sum += fromId
            if checkRepeating(fromId):
                total_sum += fromId
            fromId += 1
    print(total_sum)
