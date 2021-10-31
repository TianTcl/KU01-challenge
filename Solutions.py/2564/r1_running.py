[amt_ptcp, amt_round], ifo_speed = [int(a) for a in input().split()], list(())
for each_ptcp in range(amt_ptcp): ifo_speed.append(int(input()))
ifo_maxSpeed, amt_kick = sorted(ifo_speed)[0] * amt_round, 0
for each_ptcp in range(amt_ptcp):
    if ifo_speed[each_ptcp] * (amt_round - 1) >= ifo_maxSpeed: amt_kick += 1
print(amt_ptcp - amt_kick)
# Passed
# 100%