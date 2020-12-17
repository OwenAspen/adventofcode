file = open('C:\\py\\adventofcode2020\\day5Input.txt', 'r')
codes = file.readlines()
file.close()
highestSeatID = 0
seatID = 0
all_seatIDs = []
#part 1
for i in range(len(codes)):
    row_high = 127
    row_low = 0
    row_mid = int((row_high + row_low)/2)
    col_high = 7
    col_low = 0
    col_mid = int((col_high + col_low)/2)
    for j in range(len(codes[0])-1):
        if codes[i][j] == 'F':
            row_high = row_mid
            row_mid = int((row_high + row_low)/2)
        if codes[i][j] == 'B':
            row_low = (row_mid + 1)
            row_mid = int((row_high + row_low)/2)
        if codes[i][j] == 'L':
            col_high = col_mid
            col_mid = int((col_high + col_low)/2)
        if codes[i][j] == 'R':
            col_low = (col_mid + 1)
            col_mid = int((col_high + col_low)/2)
    seatID = (row_mid * 8 + col_mid)
    if seatID > highestSeatID:
        highestSeatID = seatID
#part 2
    all_seatIDs.append(seatID)
all_seatIDs.sort()
mySeatID = 0
for k in range(1, len(all_seatIDs)):
    if all_seatIDs[k]-1 != all_seatIDs[k-1]:
        mySeatID = all_seatIDs[k]-1

print(f'The highest seat ID is: {highestSeatID} (part 1)')
print(f'My seat ID is {mySeatID} (part 2)')
