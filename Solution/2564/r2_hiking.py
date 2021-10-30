[amt_mt, dist_l] = [int(a) for a in input().split()]
dist_m = dist_l
for each_mt in range(amt_mt):
    new_mt = int(input())
    if new_mt % 3 == 0: dist_l -= new_mt * 10 / 3
    elif new_mt % 4 == 0: dist_l -= new_mt * 5 / 2
    if new_mt % 4 == 0: dist_m -= new_mt * 5 / 2
    elif new_mt % 3 == 0: dist_m -= new_mt * 10 / 3
print(int(dist_l), int(dist_m))
# Passed
# 100%