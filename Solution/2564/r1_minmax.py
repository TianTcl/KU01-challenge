[tbl_size, cst_max], [ifo_min, ifo_max], [ifo_min2, ifo_max2] = [int(a) for a in input().split()], [{"val": 1000000}, {"val": 0}], [{"val": 1000000}, {"val": 0}]
for each_row in range(tbl_size):
    new_row = [int(b) for b in input().split()]
    if ifo_min["val"] > min(new_row): ifo_min = {"val": min(new_row), "row": each_row}
    elif ifo_min2["val"] > min(new_row) > ifo_min["val"]: ifo_min2 = {"val": min(new_row), "row": each_row}
    if ifo_max["val"] < max(new_row): ifo_max = {"val": max(new_row), "row": each_row}
    elif ifo_max2["val"] < max(new_row) < ifo_max["val"]: ifo_max2 = {"val": max(new_row), "row": each_row}
if ifo_min["row"] != ifo_max["row"]: [new_min, new_max] = [ifo_min["val"] - cst_max, ifo_max["val"] + cst_max]
elif ifo_min2["val"] - ifo_min["val"] <= abs(ifo_max["val"] - ifo_max2["val"]) and ifo_min2["val"] - ifo_min["val"] <= cst_max: [new_min, new_max] = [ifo_min2["val"] - cst_max, ifo_max["val"] + cst_max]
elif abs(ifo_min["val"] - ifo_min2["val"]) > abs(ifo_max["val"] - ifo_max2["val"]) and abs(ifo_max["val"] - ifo_max2["val"]) <= cst_max: [new_min, new_max] = [ifo_min["val"] - cst_max, ifo_max2["val"] + cst_max]
else: [new_min, new_max] = [ifo_min["val"], ifo_max["val"]]
print(abs(new_max - new_min))
# Passed
# 60% (- สามกรณี)