pin, garden_info, garden_passed = [int(a) for a in input().split()], list(()), 0
for each_rin in range(pin[0]): garden_info.append([int(b) for b in input().split()])
for each_row in range(pin[0]-4):
    for each_col in range(pin[1]-4):
        garden_plants = set(())
        for each_mrow in range(5):
            for each_mcol in range(5):
                garden_plants.add(garden_info[each_row+each_mrow][each_col+each_mcol])
        if len(garden_plants)>=5: garden_passed += 1
print(garden_passed)
# Passed
# 100%