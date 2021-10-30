floors, floor_height, questions, question_info, floor_info = int(input()), [int(a) for a in input().split()], int(input()), list(()), ["#"]
for each_floor in range(1,floors):
    for b in range(floor_height[each_floor-1]+(1 if floor_height[each_floor-1]<floor_height[each_floor] else -2), floor_height[each_floor], (1 if floor_height[each_floor-1]<floor_height[each_floor] else -1)): floor_info.append(b)
    floor_info.append("#")
for each_question in range(questions): question_info.append([int(c) for c in input().split()])
for each_seek in question_info:
    answer = [0, 0]
    for each_level in floor_info:
        if isinstance(each_level, int) and each_level>=each_seek[0] and each_level<=each_seek[1]: answer[0 if each_level%2==0 else 1] += 1
    print(answer[0]+(0 if answer[0]==0 else 1), answer[1]+(0 if answer[1]==0 else 1))
# Failed
# Unknown error