# amt_work, ifo_time, amt_day, tmp_time = int(input()), list(()), 0, 0
# for each_work in range(amt_work): ifo_time.append(int(input()))
# ifo_time.sort()
# while len(ifo_time) > 0:
#     amt_day += 1
#     if tmp_time == 0:
#         if (ifo_time[-1] > 18): tmp_time = ifo_time[-1]
#         ifo_time.pop()
#     elif sum(1 if a <= 18 else 0 for a in ifo_time) > 0:
#         ifo_time.pop(0)
#         tmp_time = 0
# print(amt_day)
# Passed
# 0% [ [TPP][TPP][PTT][TTT][TTT] ]

amt_work, amt_time = int(input()), [0, 0]
for each_work in range(amt_work): amt_time[0 if int(input()) > 18 else 1] += 1
print(sum(amt_time) if amt_time[0] <= amt_time[1] else amt_time[0] * 2 - 1)
# Passed
# 100%