travel_info = input()
battery_least = list(())
travel_line = int(travel_info.split(" ")[0])
travel_station = int(travel_info.split(" ")[1])
for specific_line in range(travel_line):
    station_info = input()
    battery_line = 0
    station_pos = station_info.split(" ")
    station_pos.insert(0, 0)
    for station_no in range(len(station_pos)-1):
        station_com_1 = int(station_pos[station_no])
        station_com_2 = int(station_pos[station_no+1])
        station_distance = station_com_2 - station_com_1
        if station_distance > battery_line:
            battery_line = station_distance
    battery_least.append(battery_line)
battery_best = dict(())
for divert_key, diver_val in enumerate(battery_least):
    battery_best[divert_key] = diver_val
for battery_com_1, specific_battery_1 in enumerate(battery_least):
    for battery_com_2, specific_battery_2 in enumerate(battery_least):
        if battery_com_1 >= battery_com_2:
            pass
        elif battery_com_1 < battery_com_2:
            if specific_battery_1 <= specific_battery_2:
                try:
                    battery_best.pop(battery_com_2)
                except:
                    pass
            elif specific_battery_1 > specific_battery_2:
                try:
                    battery_best.pop(battery_com_1)
                except:
                    pass
for battery_answer in battery_best:
    battery_choose = battery_best[battery_answer]
print(battery_choose)
# Passed