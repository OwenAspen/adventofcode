file = open('C:\\py\\adventofcode2020\\Day4Input.txt', 'r')
data = file.read()
file.close()
passports = data.split('\n\n')
passportFields = []
goodPassports = 0
passportListDict = []
#part 1
for i in range(len(passports)):
    passportList = passports[i].split()
    passportFields.clear()
    for j in range(len(passportList)):
        passportFields.append(passportList[j][0:4])
        if 'cid:' in passportFields:
            passportFields.remove('cid:')
    if len(passportFields) >= 7:
        goodPassports +=1
#part 2
        passDict = {}
        for x in range(len(passportList)):
            passDict[passportList[x][0:4]] = passportList[x][4:]
        passportListDict.append(passDict)
eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
validPassports = 0
for y in range(len(passportListDict)):
    validCount = 0
    if  1920 <= int(passportListDict[y]['byr:']) <= 2002:
        validCount += 1
    if 2010 <= int(passportListDict[y]['iyr:']) <= 2020:
        validCount += 1
    if 2020 <= int(passportListDict[y]['eyr:']) <= 2030:
        validCount += 1
    if passportListDict[y]['hgt:'][3:] == 'cm' and 150 <= int(passportListDict[y]['hgt:'][0:3]) <= 193:
        validCount += 1
    if passportListDict[y]['hgt:'][2:] == 'in' and 59 <= int(passportListDict[y]['hgt:'][0:2]) <= 76:
        validCount += 1
    if passportListDict[y]['hcl:'][0] == '#' and len(passportListDict[y]['hcl:']) == 7 and passportListDict[y]['hcl:'][1:].isalnum():
        validCount += 1
    if passportListDict[y]['ecl:'] in eyeColors:
        validCount += 1
    if len(passportListDict[y]['pid:']) == 9:
        validCount += 1
    if validCount == 7:
        validPassports += 1
print(f'There are {goodPassports} passports with enough fields. (part 1)')
print(f'There are {validPassports} passports with enough fields and valid entries in those fields. (part 2)')
