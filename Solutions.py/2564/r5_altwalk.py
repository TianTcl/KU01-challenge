# ifo_size, ifo_board, amt_walk = int(input()), list(()), 1
# for each_row in range(ifo_size): ifo_board.append([(False if a=="." else True) for a in input()])
# def path_find(coord_x, coord_y, coord_s):
#     global ifo_board, amt_walk
#     if not (ifo_board[coord_y][coord_x] == None or coord_y + 1 == ifo_size or coord_x + 1 == ifo_size):
#         if coord_x - 1 >= 0 and ifo_board[coord_y][coord_x - 1] != None: path_find(coord_x - 1, coord_y, ifo_board[coord_y][coord_x])
#         if coord_y - 1 >= 0 and ifo_board[coord_y - 1][coord_x] != None: path_find(coord_x, coord_y - 1, ifo_board[coord_y][coord_x])
#         if coord_x + 1 < ifo_size and ifo_board[coord_y][coord_x + 1] != None: path_find(coord_x + 1, coord_y, ifo_board[coord_y][coord_x])
#         if coord_y + 1 < ifo_size and ifo_board[coord_y + 1][coord_x] != None: path_find(coord_x, coord_y + 1, ifo_board[coord_y][coord_x])
#         coord_s = not coord_s
#         if ifo_board[coord_y][coord_x + 1] == coord_s:
#             amt_walk += 1
#             ifo_board[coord_y][coord_x + 1] = None
#         if ifo_board[coord_y + 1][coord_x] == coord_s:
#             amt_walk += 1
#             ifo_board[coord_y + 1][coord_x] = None
#         ifo_board[coord_y][coord_x] = None
# path_find(0, 0, ifo_board[0][0])
# print(amt_walk)

ifo_size, ifo_board = int(input()), list(())
for each_row in range(ifo_size): ifo_board.append([(0 if a=="." else 1) for a in input()])
ifo_board[0][0] += 2
def check_cell(each_row):
    global ifo_board, ifo_size
    for each_col in range(ifo_size):
        tmp_cond = [
            each_row > 0 and abs(ifo_board[each_row][each_col] - ifo_board[each_row - 1][each_col]) % 2 == 1 and ifo_board[each_row - 1][each_col] > 1,
            each_row + 1 < ifo_size and abs(ifo_board[each_row][each_col] - ifo_board[each_row + 1][each_col]) % 2 == 1 and ifo_board[each_row + 1][each_col] > 1,
            each_col > 0 and abs(ifo_board[each_row][each_col] - ifo_board[each_row][each_col - 1]) % 2 == 1 and ifo_board[each_row][each_col - 1] > 1,
            each_col + 1 < ifo_size and abs(ifo_board[each_row][each_col] - ifo_board[each_row][each_col + 1]) % 2 == 1 and ifo_board[each_row][each_col + 1] > 1
        ]
        if ifo_board[each_row][each_col] < 2 and True in tmp_cond: ifo_board[each_row][each_col] += 2
for each_row in range(ifo_size): check_cell(each_row)
for each_row in range(ifo_size - 1, -1, -1): check_cell(each_row)
print(sum([ifo_board[b].count(2) + ifo_board[b].count(3) for b in range(ifo_size)]))
# Unknown error