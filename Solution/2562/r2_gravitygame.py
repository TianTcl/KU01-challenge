game_space = int(input())
block_input = list(())
block_left = list(())
block_down = list(())
for game_row in range(game_space):
    block_input.append(list(input()))
for rock_row in range(len(block_input)):
    row_count = block_input[rock_row].count("#")
    row_list = list(())
    for row_rock in range(row_count):
        row_list.append("#")
    for row_air in range(game_space-row_count):
        row_list.append(".")
    block_left.append(row_list)
for game_area in range(game_space):
    block_down.append(list(()))
for rock_col in range(len(block_left)):
    col_rock = 0
    col_air = 0
    for col_row in range(len(block_left)):
        col_get = block_left[col_row][rock_col]
        if col_get == "#":
            col_rock += 1
        elif col_get == ".":
            col_air += 1
    for col_roll in range(len(block_down)):
        if col_air > 0:
            block_down[col_roll].append(".")
            col_air -= 1
        elif col_rock > 0:
            block_down[col_roll].append("#")
            col_rock -= 1
for game_result in range(len(block_down)):
    block_space = block_down[game_result]
    for blocks in block_space:
        print(blocks, end="")
    print("")
# Passed