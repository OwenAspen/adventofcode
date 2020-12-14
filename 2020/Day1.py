file = open('C:\\py\\adventofcode2020\\Day1Input.txt', 'r')
nums = file.readlines()
file.close()
#print(nums)

#part 1
for x in range(len(nums)):
    for y in range(len(nums)):
        if int(nums[x]) + int(nums[y]) == 2020:
            firstNum = int(nums[x])
            secondNum = int(nums[y])
answer1 = firstNum * secondNum
print(answer1)

#part 2
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if int(nums[i]) + int(nums[j]) + int(nums[k]) == 2020:
                num1 = int(nums[i])
                num2 = int(nums[j])
                num3 = int(nums[k])
answer2 = num1*num2*num3
print(answer2)
