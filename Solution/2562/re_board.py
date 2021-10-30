info_init = input()
room_row = int(info_init.split(" ")[0])
room_col = int(info_init.split(" ")[1])
room_dif = int(info_init.split(" ")[2])
seat_room = []
info_visible = room_col
info_new = []
for each_info_new in range(room_col):
    info_new.append([])
for each_row in range(room_row):
    seat_row = input().split(" ")
    new_seat = []
    for each_seat in seat_row:
        seat_height = int(each_seat)
        new_seat.append(seat_height)
    seat_room.append(new_seat)
for each_inv_col in range(room_col):
    for each_inv_row in range(room_row):
        get_col = info_new[each_inv_col]
        get_col.append(seat_room[each_inv_row][each_inv_col])
        info_new[each_inv_col] = get_col
for each_col in info_new:
    new_height = []
    for each_std in range(len(each_col)):
        new_height.append(each_col[each_std] + room_dif * each_std)
    for com_std in range(len(new_height) - 1):
        com_std_a  = new_height[com_std + 1]
        com_std_r = []
        for com_std_o in range(com_std + 1):
            com_std_b = new_height[com_std_o]
            
            if com_std_a > com_std_b:
                com_std_r.append(1)
            else:
                com_std_r.append(0)
        if com_std_r.count(0) == 0:
            info_visible += 1
print(info_visible)
# Passed