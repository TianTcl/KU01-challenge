bear_count = int(input())
good_bear = 0
for specific_bear in range(bear_count):
    bear_validation = input()
    bear_weight = int(bear_validation.split(" ")[0])
    bear_perfection = int(bear_validation.split(" ")[1])
    if bear_perfection >= 80 and bear_perfection <= 100 and bear_weight >= 100 and bear_weight <= 750:
        good_bear += 1
print(good_bear)
# Passed