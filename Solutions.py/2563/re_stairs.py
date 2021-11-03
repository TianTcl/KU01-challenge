# floors, floor_height, questions, question_info, floor_info = int(input()), [int(a) for a in input().split()], int(input()), list(()), ["#"]
# for each_floor in range(1,floors):
#     for b in range(floor_height[each_floor-1]+(1 if floor_height[each_floor-1]<floor_height[each_floor] else -2), floor_height[each_floor], (1 if floor_height[each_floor-1]<floor_height[each_floor] else -1)): floor_info.append(b)
#     floor_info.append("#")
# for each_question in range(questions): question_info.append([int(c) for c in input().split()])
# for each_seek in question_info:
#     answer = [0, 0]
#     for each_level in floor_info:
#         if isinstance(each_level, int) and each_level>=each_seek[0] and each_level<=each_seek[1]: answer[0 if each_level%2==0 else 1] += 1
#     print(answer[0]+(0 if answer[0]==0 else 1), answer[1]+(0 if answer[1]==0 else 1))
# Failed
# Unknown error

# amt_room, ifo_room, amt_range, ifo_range, ifo_stair = int(input()), [int(a) for a in ("0 "+input()).split()], int(input()), list(()), list(())
# for each_range in range(amt_range): ifo_range.append([int(b) for b in input().split()])
# for each_room in range(amt_room): ifo_stair.extend([c for c in range(ifo_room[each_room]+(1 if ifo_room[each_room]<ifo_room[each_room+1] else -1), ifo_room[each_room+1], (1 if ifo_room[each_room]<ifo_room[each_room+1] else -1))])
# for each_range in range(amt_range): print(len(list(filter(lambda d: d >= ifo_range[each_range][0] and d <= ifo_range[each_range][1] and d % 2 == 0, ifo_stair))), len(list(filter(lambda d: d >= ifo_range[each_range][0] and d <= ifo_range[each_range][1] and d % 2 == 1, ifo_stair))))
# Passed
# 10% [[PPP][xxxx][TTT][xxxxxxx]]

amt_room, ifo_room, amt_range, ifo_stair = int(input()), [int(a) for a in ("0 "+input()).split()], int(input()), list(())
for each_room in range(amt_room): ifo_stair.extend([c for c in range(ifo_room[each_room]+(1 if ifo_room[each_room]<ifo_room[each_room+1] else -1), ifo_room[each_room+1], (1 if ifo_room[each_room]<ifo_room[each_room+1] else -1))])
for each_range in range(amt_range):
    ifo_range = [int(b) for b in input().split()]
    print(len(list(filter(lambda d: d >= ifo_range[0] and d <= ifo_range[1] and d % 2 == 0, ifo_stair))), len(list(filter(lambda d: d >= ifo_range[0] and d <= ifo_range[1] and d % 2 == 1, ifo_stair))))
# Passed
# 10% [[PPP][xxxx][TTT][xxxxxxx]]