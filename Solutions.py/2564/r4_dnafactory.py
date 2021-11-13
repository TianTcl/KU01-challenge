# [amt_dna, amt_req], ifo_req, amt_huge = [int(a) for a in input().split()], list(()), 0
# for each_req in range(amt_req): ifo_req.append([int(b) for b in input().split()])
# for each_req in ifo_req:
#     new_check = 0
#     for each_comp in ifo_req:
#         if each_req != each_comp and (each_req[0] <= each_comp[0] <= each_req[1] or each_req[0] <= each_comp[1] <= each_req[1]): new_check += 1
#     amt_huge = max(amt_huge, new_check)
# print(amt_huge)
# Failed
# 0% [-----TTTTT]

[amt_dna, amt_req], amt_huge = [int(a) for a in input().split()], 0
ifo_req, ifo_dup = dict([(int(b), []) for b in range(amt_dna)]), dict([(int(c), 0) for c in range(amt_dna)])
for each_req in range(amt_req):
    [ifo_start, ifo_stop] = [int(d) for d in input().split()]
    for ifo_pos in range(ifo_start, ifo_stop):
        ifo_req[ifo_pos].append(each_req)
        ifo_dup[ifo_pos] += 1
for each_req in ifo_req.values():
    if set(ifo_req[list(ifo_dup.values()).index(max(ifo_dup.values()))]).issubset(set(each_req)): amt_huge = max(amt_huge, len(set(each_req)))
print(amt_huge)
# Passed
# 30% [ --PPPTTTTT ]