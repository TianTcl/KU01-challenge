amt_log, ifo_log = int(input()), dict(())
for each_log in range(amt_log): ifo_log[each_log+1] = [int(a) for a in input().split()]
for each_log in reversed(ifo_log.keys()):
    if ifo_log[each_log][0] == 0: ifo_log[each_log][1] = ifo_log[ifo_log[each_log][1]]
    if ifo_log[each_log][2] == 0: ifo_log[each_log][3] = ifo_log[ifo_log[each_log][3]]
ifo_log, amt_add = ifo_log[1], 0
def amt_sum(ifo_tree):
    global amt_add
    amt_max = 0
    if ifo_tree[0] == 1 and ifo_tree[2] == 1:
        tmp_1, tmp_2 = ifo_tree[1], ifo_tree[3]
    elif ifo_tree[0] == 0 and ifo_tree[2] == 1:
        tmp_1, tmp_2 = amt_sum(ifo_tree[1]), ifo_tree[3]
    elif ifo_tree[0] == 1 and ifo_tree[2] == 0:
        tmp_1, tmp_2 = ifo_tree[1], amt_sum(ifo_tree[3])
    elif ifo_tree[0] == 0 and ifo_tree[2] == 0:
        tmp_1, tmp_2 = amt_sum(ifo_tree[1]), amt_sum(ifo_tree[3])
    if (tmp_1 > tmp_2): amt_add += tmp_1 - tmp_2
    elif (tmp_1 < tmp_2): amt_add += tmp_2 - tmp_1
    amt_max = max(tmp_1, tmp_2) * 2
    return amt_max
amt_sum(ifo_log)
print(amt_add)
# Passed
# 100%