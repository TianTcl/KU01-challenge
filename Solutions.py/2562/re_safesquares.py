init_info = input().split(" ")
sapce_width = int(init_info[0])
space_length = int(init_info[1])
space_gun = int(init_info[2])
gun_x = []
gun_y = []
for each_input in range(space_gun):
    init_gun = input().split()
    gun_x.append(int(init_gun[0]))
    gun_y.append(int(init_gun[1]))
new_width = sapce_width - len(set((gun_x)))
new_length = space_length - len(set((gun_y)))
print((new_width * new_length) % 25621)
# Passed