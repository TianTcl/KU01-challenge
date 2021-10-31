[amt_ppl, amt_cap] = [int(a) for a in input().split()]
place_queue = [0 for b in range(amt_cap)]
for each_ppl in range(amt_ppl): place_queue[int(input())-1] += 1
amt_arranged, amt_left = sorted(place_queue), 0
for each_row in range(len(amt_arranged)-1): amt_left += amt_arranged[each_row+1] - amt_arranged[0]
print(amt_left)
# Passed
# 100%