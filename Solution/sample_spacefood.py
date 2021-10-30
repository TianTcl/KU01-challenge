[day_survive, food_death, food_hunger], food_retrieve, food_has, day_hunger = [int(a) for a in input().split()], [int(b) for b in input().split()], 0, 0
food_hunger -= food_death
for each_day in range(day_survive):
    food_has += food_retrieve[each_day] - food_death
    if (food_has < 0):
        day_hunger = -1
        break
    elif (food_has < food_hunger):
        food_has = 0
        day_hunger += 1
    elif (food_has >= food_hunger): food_has -= food_hunger
    else: day_hunger += 1
print(day_hunger)