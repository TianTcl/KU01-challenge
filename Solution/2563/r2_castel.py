cur_room, cur_lyr = int(input()), 0
while cur_lyr**2<cur_room: cur_lyr+=1
print((cur_lyr-2)*2+(2 if cur_room%2==cur_lyr%2 else 1))
# Passed