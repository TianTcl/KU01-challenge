[amt_dna, amt_req], ifo_req, amt_huge = [int(a) for a in input().split()], list(()), 0
for each_req in range(amt_req): ifo_req.append([int(b) for b in input().split()])
for each_req in ifo_req:
    new_check = 0
    for each_comp in ifo_req:
        if each_req != each_comp and (each_req[0] <= each_comp[0] <= each_req[1] or each_req[0] <= each_comp[1] <= each_req[1]): new_check += 1
    amt_huge = max(amt_huge, new_check)
print(amt_huge)
# Failed
# 0% [-----TTTTT]