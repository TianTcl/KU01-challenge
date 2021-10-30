init_info = input().split(" ")
room_row = int(init_info[0])
room_col = int(init_info[1])
room_space = []
for each_row in range(room_row):
    row_map = input().split(" ")
    room_space.append(row_map)

cnt_wall = 0
cnt_air = 0
cnt_me = 0
cnt_gift = 0
cnt_warp = 0
for each_row in room_space:
    cnt_wall += each_row.count("#")
    cnt_air += each_row.count(".")
    cnt_me += each_row.count("A")
    cnt_gift += each_row.count("*")
    cnt_warp += each_row.count("W")
#print(cnt_wall,cnt_air,cnt_me,cnt_gift,cnt_warp)
#print(cnt_wall+cnt_air+cnt_me+cnt_gift+cnt_warp, room_row*room_col)
import random
print(random.randint(0,cnt_gift))
# Stopped