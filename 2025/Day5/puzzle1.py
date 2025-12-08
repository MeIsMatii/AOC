inputFile = '/workspaces/AOC/2025/Day5/testInput.txt'

list = []
with open(inputFile, 'r') as file:
    for line in file:
        line = line.strip()
        ranges = line.split('-')
        list.append(ranges)

productIds = []
idRanges = []
check = False
for i in range (len(list)):
    if list[i][0] == '':
        check = True
        continue
    if not check: 
        idRanges.append(list[i])
    else:
        productIds.append(list[i])


validProducts = 0
check = False
for idIndex in range(len(productIds)): 
    product = int(productIds[idIndex][0])
    for i in range(len(idRanges)):
        if product < int(idRanges[i][0]) or product > int(idRanges[i][1]):
            continue
        else:
            validProducts += 1
            break

print(validProducts)