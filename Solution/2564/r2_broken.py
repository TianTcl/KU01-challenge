board_size, board_info, board_good = int(input()), list(()), 1
for each_row in range(board_size): board_info.append([(None if a=="." else False) for a in input()])
def path_find(coord_x, coord_y):
    global board_info
    if board_info[coord_y][coord_x] != False:
        if coord_y + 1 == board_size and coord_x + 1 == board_size: return True
        possible_x = path_find(coord_x + 1, coord_y) if coord_x + 1 < board_size and board_info[coord_y][coord_x + 1] != False else False
        possible_y = path_find(coord_x, coord_y + 1) if coord_y + 1 < board_size and board_info[coord_y + 1][coord_x] != False else False
        board_info[coord_y][coord_x] = possible_x or possible_y
        return possible_x or possible_y
    else: return False
path_find(0, 0)
# def path_patch(board_row):
#     global board_info
#     if None in board_info[board_row]:
#         path_find(board_info[board_row].index(None), board_row)
#         if None in board_info[board_row]: return path_patch(board_row)
#     else: return True
for each_row in range(board_size):
    # while path_patch(each_row): pass
    if None in board_info[each_row]: path_find(board_info[each_row].index(None), each_row)
    board_good += board_info[each_row].count(True)
print(board_good)
# Passed
# 30% [ PP-P-----T ]