file = open('C:\\py\\adventofcode2020\\day6Input.txt','r')
answers_raw = file.read()
file.close()
#part 1
group_list = []
answers_list = answers_raw.split('\n\n')
for i in range(len(answers_list)):
    group_list.append(answers_list[i].split('\n'))
sum_GC = 0
for x in range(len(group_list)):
    group_answer_list = []
    for y in range(len(group_list[x])):
        for z in range(len(group_list[x][y])):
            if group_list[x][y][z] not in group_answer_list:
                group_answer_list.append(group_list[x][y][z])
    sum_GC += len(group_answer_list)
print(f'The sum of all group yes answers is {sum_GC} (part 1)')
#part 2
sum_all_yes = 0
for x in range(len(group_list)):
    all_group_ans = []
    all_yes = []
    for y in range(len(group_list[x])):
        for z in range(len(group_list[x][y])):
            all_group_ans.append(group_list[x][y][z])
    for char in all_group_ans:
        if all_group_ans.count(char) == len(group_list[x]) and char not in all_yes:
            all_yes.append(char)
    sum_all_yes += len(all_yes)
print(f'The sum of all unanimous yes answers is {sum_all_yes} (part 2)')
