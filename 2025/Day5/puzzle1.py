inputFile = '/home/mati/Documents/AOC/2025/Day5/testInput.txt'

idRanges = []
with open(inputFile, 'r') as file:
    for line in file:
        line = line.strip()
        ranges = line.splig('-')
        idRanges.append(ranges)

        