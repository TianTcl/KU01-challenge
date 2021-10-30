main_input = input()
robot_count = int(main_input.split(" ")[0])
max_height = int(main_input.split(" ")[1])
robot_height = 0
for specific_robot in range(robot_count):
    robot_power = int(input())
    if robot_power <= max_height and robot_power > robot_height:
        robot_height = robot_power
print(robot_height)
# Passed