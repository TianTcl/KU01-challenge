info_init = input()
plane_width = int(info_init.split(" ")[0])*2
plane_length = int(info_init.split(" ")[1])
plane_cmd = int(info_init.split(" ")[2])
info_result = []
for each_path in range(plane_cmd):
    rbt_pos_x = plane_width/2
    rbt_pos_y = plane_length
    rbt_cmd = input().split(" ")
    rbt_live = []
    for each_cmd in rbt_cmd:
        if each_cmd == "0":
            rbt_pos_x -= 1
        elif each_cmd == "1":
            rbt_pos_x += 1
        if rbt_pos_x >= 0 and rbt_pos_x <= plane_width:
            rbt_live.append(1)
        else:
            rbt_live.append(0)
    rbt_path_forward = len(rbt_cmd)
    rbt_pos_end = [rbt_live.count(0), rbt_pos_y - rbt_path_forward]
    if rbt_pos_end[0] == 0 and rbt_pos_end[1] >= 0:
        info_result.append(1)
    else:
        info_result.append(0)
for each_result in info_result:
    print(each_result)
# Passed