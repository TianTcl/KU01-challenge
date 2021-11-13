# Search all
[size_x, size_y, amt_obj], ifo_obj, amt_place, size_tbl = [int(a) for a in input().split()], list(()), 0, 3
for each_obj in range(amt_obj): ifo_obj.append([int(b)-1 for b in input().split()])
for each_y in range(size_y - size_tbl):
    for each_x in range(size_x - size_tbl):
        new_check = set(())
        for each_obj in ifo_obj: new_check.add( not (
            # Corner in obj
            (each_obj[0] < each_x < each_obj[2] and each_obj[1] < each_y < each_obj[3]) or
            (each_obj[0] < each_x + size_tbl < each_obj[2] and each_obj[1] < each_y < each_obj[3]) or
            (each_obj[0] < each_x < each_obj[2] and each_obj[1] < each_y + size_tbl < each_obj[3]) or
            (each_obj[0] < each_x + size_tbl < each_obj[2] and each_obj[1] < each_y + size_tbl < each_obj[3]) or
            # Obj in table
            # ((each_x < each_obj[0] < each_x + size_tbl or each_x < each_obj[2] < each_x + size_tbl) and
            # (each_y < each_obj[1] < each_y + size_tbl or each_y < each_obj[3] < each_y + size_tbl))
            (each_x <= each_obj[0] < each_obj[2] <= each_x + size_tbl and each_y <= each_obj[1] < each_obj[3] <= each_y + size_tbl)
        ) )
        if False not in new_check: amt_place += 1
print(amt_place)

# Search by row
# [size_x, size_y, amt_obj], ifo_obj, amt_place, size_tbl = [int(a) for a in input().split()], list(()), 0, 3
# for each_obj in range(amt_obj): ifo_obj.append([int(b)-1 for b in input().split()])
# for each_y in range(size_y):
#     for each_x in range(size_x - size_tbl):
#         new_check = set(())
#         for each_obj in ifo_obj: 
#             if (each_obj[1] <= each_y <= each_obj[3]): new_check.add(not(each_x <= each_obj[0] < each_x + 3 or each_x < each_obj[2] <= each_x + 3))
#         if False not in new_check: amt_place += 1
# print(amt_place)

# Stopped
# Unknown error @ possibility check