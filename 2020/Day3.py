file = open('C:\\py\\adventofcode2020\\Day3Input.txt', 'r')
lines = file.readlines()
file.close()
tmap = []
for i in range(len(lines)):
    tmap.append(lines[i].strip())
#print(tmap)

def treeCount(right, down):
    treeEncounters = 0

    x = 0
    y = 0
    while y < len(tmap):

        x = x % len(tmap[0])

        if tmap[y][x] == '#':
            treeEncounters += 1
        x += right
        y += down
    print(treeEncounters)
#part1
treeCount(3,1)
#part2
treeCount(1,1)
treeCount(5,1)
treeCount(7,1)
treeCount(1,2)

