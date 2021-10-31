array_count = int(input())
junction_prize = input()
junction_rem = dict(())
money_most = list(())
junction_edit = junction_prize.split(" ")
for divert_junction, divert_prize in enumerate(junction_edit):
    junction_rem[divert_junction+1] = int(divert_prize)
#junction_unknown = junction_edit.count("0")
#junction_log = dict(())
#for juncton_change in range(junction_unknown):
#    junction_new = junction_unknown - juncton_change
for array_path in range(1, array_count):
    money_array = []
    for money_north in range(1, array_path+1):
        money_array.append(junction_rem[money_north])
    for money_south in range(2*array_count-array_path+1, 2*array_count):
        money_array.append(junction_rem[money_south])
    money_all = {x for x in range(1, 2*array_count)}
    money_same = money_all.intersection(money_array)
    money_left = list((money_all - money_same))
    for edit_north in range(1, array_path+1):
        if int(junction_rem[edit_north]) == 0:
            junction_rem[edit_north] = money_left[0]
            money_left.pop(0)
    for edit_south in range(2*array_count-array_path+1, 2*array_count):
        if int(junction_rem[edit_south]) == 0:
            junction_rem[edit_south] = money_left[0]
            money_left.pop(0)
    money_total = 0
    for junction_north in range(1, array_path+1):
        money_total += junction_rem[junction_north]
    for junction_south in range(2*array_count-array_path+1, 2*array_count):
        money_total += junction_rem[junction_south]
    money_most.append(money_total)
for money_each in money_most:
    money_choose = money_each
print(money_choose)
# Failed