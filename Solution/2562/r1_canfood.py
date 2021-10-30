can_count = int(input())
good_can = 0
for specific_can in range(can_count):
    can_validation = input()
    can_life = int(can_validation.split(" ")[0])
    can_weight = int(can_validation.split(" ")[1])
    if can_life <= 400 and can_weight >= 150 and can_weight <= 200:
        good_can += 1
print(good_can)
# Passed