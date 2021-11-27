# amt_hole, ifo_hole = int(input()), {"lx": float("inf"), "ly": float("inf"), "hx": float("-inf"), "hy": float("-inf")}
# for each_hole in range(amt_hole):
#     ifo_pos = [int(a) for a in input().split()]
#     ifo_hole["lx"] = min(ifo_hole["lx"], ifo_pos[0])
#     ifo_hole["hx"] = max(ifo_hole["hx"], ifo_pos[0])
#     ifo_hole["ly"] = min(ifo_hole["ly"], ifo_pos[1])
#     ifo_hole["hy"] = max(ifo_hole["hy"], ifo_pos[1])
# print(max(ifo_hole["lx"]*ifo_hole["ly"], ifo_hole["lx"]*ifo_hole["hy"], ifo_hole["hx"]*ifo_hole["ly"], ifo_hole["hx"]*ifo_hole["hy"]))
# Misdirection: "SQUARE" not "RECTANGLE"

amt_hole, ifo_hole, ifo_max = int(input()), list(()), 0
for each_hole in range(amt_hole): ifo_hole.append([int(a) for a in input().split()])
for each_hole1 in ifo_hole:
    for each_hole2 in ifo_hole:
        if abs(each_hole1[0] - each_hole2[0]) > 0 and abs(each_hole1[0] - each_hole2[0]) == abs(each_hole1[1] - each_hole2[1]): ifo_max = max(ifo_max, abs(each_hole1[0] - each_hole2[0]))
print(ifo_max)
# Passed
# 50% (T ห้าตัว)