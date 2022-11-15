import copy
[sizeY, sizeX, paths], field = [int(_) for _ in input().split()], []
for _ in range(sizeY): field.append([_=="." for _ in input()])
def find(frX, frY, toX, toY, dir=None):
    global sizeY, sizeX, field, level, path, stY
    if abs(frY-stY)>level or not field[frY][frX] or not path[frY][frX]: return False
    elif frX==toX and frY==toY: return True
    else:
        path[frY][frX], reach = False, False
        if frX>0 and dir!=2: reach = reach or find(frX-1, frY, toX, toY, 4)
        if frY>0 and dir!=3: reach = reach or find(frX, frY-1, toX, toY, 1)
        if frX<sizeX-1 and dir!=4: reach = reach or find(frX+1, frY, toX, toY, 2)
        if frY<sizeY-1 and dir!=1: reach = reach or find(frX, frY+1, toX, toY, 3)
        return reach
for path in range(paths):
    frY, frX, toY, toX, level = [int(_)-1 for _ in input().split()]
    level, stY = level+1, frY
    if abs(frY-toY)>level: print(0)
    else:
        path = copy.deepcopy(field)
        print(1 if find(frX, frY, toX, toY, 0) else 0)
# Passed