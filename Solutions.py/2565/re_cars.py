# amount, top, waste = int(input()), int(input().split()[1]), 0
# for each in range(amount-1):
#     car = int(input().split()[1])
#     if car>=top: waste += 1
#     else: top = car
# print(waste)
# Passed 20%
# PP---[--P---PP]

amount, waste, info = int(input()), 0, []
for _ in range(amount): info.append([int(_) for _ in input().split()])
for each in range(amount):
    for comp in range(each+1, amount):
        if (info[amount-comp-1][0]>=info[amount-each-1][0] and info[amount-comp-1][1]<=info[amount-each-1][1]): waste += 1
print(waste)
# Passed 0%