tile_length = int(input())
path_input = list(input())
tile_half = tile_length//2
path_least = tile_length
for path_remove in range(tile_half - 1):
    tile_left = tile_half - path_remove - 1
    tile_right = tile_half + path_remove
    if path_input[tile_left] == "#":
        path_least = tile_left
        break
    elif path_input[tile_right] == "#":
        path_least = tile_right
        break
if tile_length - path_least > path_least:
    path_least = tile_length - path_least -1
print(path_least)
# Passed