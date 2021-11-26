amt_torch, ifo_light, amt_max, ifo_count, ifo_dgree  = int(input()), [False for a in range(360)], 0, 0, 0
def fill_light(ifo_start, ifo_stop):
    for each_spot in range(ifo_start, ifo_stop): ifo_light[each_spot] = True
for each_torch in range(amt_torch):
    [ifo_start, ifo_stop] = [int(b) for b in input().split()]
    if ifo_stop > ifo_start: fill_light(ifo_start, ifo_stop)
    else:
        fill_light(ifo_start, 360)
        fill_light(0, ifo_stop)
while (ifo_dgree <= 360 or ifo_light[ifo_dgree%360]) and amt_max < 360:
    ifo_count = ifo_count + 1 if ifo_light[ifo_dgree%360] else 0
    amt_max, ifo_dgree = max(amt_max, ifo_count), ifo_dgree + 1
print(amt_max)
# Passed
# 100%