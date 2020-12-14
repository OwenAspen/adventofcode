file = open('C:\\py\\adventofcode2020\\Day2Input.txt', 'r')
data = file.readlines()
file.close()
#print(data)
validPass = 0
for i in range(len(data)):
    lowerRange = data[i][0:data[i].index('-')]
    upperRange = data[i][data[i].index('-')+1:data[i].index(' ')]
    checkLetter = data[i][data[i].index(' ')+1]
    passToCheck = data[i][data[i].index(':')+1:len(data[i])-1]
    letterCheckCount = 0
 # PART 1:
    '''
    for j in range(len(passToCheck)):
        if passToCheck[j] == checkLetter:
            letterCheckCount += 1
    if letterCheckCount >= int(lowerRange) and letterCheckCount <= int(upperRange):
        validPass += 1

    '''
# PART 2:

    if passToCheck[int(lowerRange)] == checkLetter:
        validPass += 1
    if len(passToCheck) > int(upperRange):
        if passToCheck[int(upperRange)] == checkLetter:
            validPass += 1
        if passToCheck[int(lowerRange)] == checkLetter and passToCheck[int(upperRange)] == checkLetter:
            validPass -= 2

print(validPass)
