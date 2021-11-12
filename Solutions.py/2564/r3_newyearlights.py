[amt_bulb, amt_rule], ifo_rule = [int(a) for a in input().split()], list(())
ifo_bulb = [False if b > 0 else True for b in range(amt_bulb)]
for each_rule in range(amt_rule):
    new_rule = [int(c)-1 for c in input().split()]
    ifo_rule.append({
        "req": new_rule[:-1],
        "set": new_rule[-1]
    })
del new_rule, amt_bulb, amt_rule
while True:
    tmp_bulb = ifo_bulb.copy()
    for each_rule in ifo_rule:
        if False not in set([ifo_bulb[d] for d in each_rule["req"]]): ifo_bulb[each_rule["set"]] = True
    if tmp_bulb == ifo_bulb: break
print(ifo_bulb.count(True))
# Passed
# 0% [----------]