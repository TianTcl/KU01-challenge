import math
[amt_layer, ifo_width, ifo_drop] = [int(a) for a in input().split()]
ifo_width = ifo_width * 2 - 1
if ifo_drop - amt_layer > 0 and ifo_drop + amt_layer <= ifo_width: ifo_layer = [math.comb(amt_layer, b) for b in range(amt_layer + 1)]
else:
    ifo_layer = list(())
    for each_layer in range(1, amt_layer + 1):
        if len(ifo_layer) > 0 or ifo_drop + each_layer > ifo_width or ifo_drop - each_layer < 1:
            if not len(ifo_layer): ifo_layer = [math.comb(each_layer - 1, c) for c in range(each_layer)]
            tmp_layer = list(())
            tmp_layer.append(ifo_layer[0] * (2 if (tmp_cond := each_layer % 2 == 1 and ifo_drop - each_layer < 1) else 1))
            if tmp_cond: tmp_layer[0] += ifo_layer[1]
            for each_drop in range(1 if tmp_cond else 0, len(ifo_layer) - 1): tmp_layer.append(ifo_layer[each_drop] + ifo_layer[each_drop + 1])
            if ifo_drop + each_layer > ifo_width and each_layer % 2 == 1: tmp_layer[-1] += ifo_layer[-1]
            else: tmp_layer.append(ifo_layer[-1])
            ifo_layer = tmp_layer
if ifo_drop - amt_layer > 1 and (ifo_drop - amt_layer + 1) // 2 > 1: ifo_layer = [0 for d in range((ifo_drop - amt_layer + 1) // 2 - 1)] + ifo_layer
if ifo_drop + amt_layer < ifo_width and (ifo_width - ifo_drop - amt_layer + 1) // 2 > 0: ifo_layer = ifo_layer + [0 for d in range((ifo_width - ifo_drop - amt_layer + 1) // 2)]
print(*ifo_layer, sep=" ")
# Passed
# 80% [P-PPPxPPPP]