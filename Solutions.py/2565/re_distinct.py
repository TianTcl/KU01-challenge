amount, prices = int(input()), [int(_) for _ in input().split()]
sums = set(prices)
for start in range(0, amount):
    for stop in range(start, amount):
        sums.add(sum(prices[start:stop+1]))
print(len(sums))
# Passed