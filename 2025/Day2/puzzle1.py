testinput = [11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124]
# with open('puzzleInput.txt', 'r') as file:
#     for line in file:
#         line = line.strip()
#         line = line.split(",")
line = testinput 
for i in testinput:
    idRange = line[i].split("-")
    fromId = idRange[0]
    toId = idRange[1]