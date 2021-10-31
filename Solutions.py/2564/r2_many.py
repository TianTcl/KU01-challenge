[amt_wall, amt_min], amt_mess = [int(a) for a in input().split()], 0
for each_wall in range(amt_wall):
    if len(set([int(b) for b in input().split()])) > amt_min: amt_mess += 1
print(amt_mess)