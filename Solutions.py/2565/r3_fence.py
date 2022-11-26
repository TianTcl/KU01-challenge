[height, width, questions], info, levels = map(int, input().split()), {}, set()
for row in range(height):
    flowers = [int(_) for _ in input().split()]
    levels = levels.union(set(flowers))
    for col, level in enumerate(flowers):
        if level==0: continue
        elif level in info.keys(): info[level] = [min(info[level][0], row), max(info[level][1], row), min(info[level][2], col), max(info[level][3], col)]
        else: info[level] = [row, row, col, col]
levels = list(levels)
levels.sort()
for _ in range(questions):
    mode, search = map(int, input().split())
    if mode==1: print(0 if search not in info.keys()else(info[search][1]-info[search][0]+info[search][3]-info[search][2]+2)*2)
    else:
        query = False
        for flower in levels:
            if (flower < search or flower not in info.keys()): continue
            elif query == False: query = info[flower]
            else: query = [min(info[flower][0], query[0]), max(info[flower][1], query[1]), min(info[flower][2], query[2]), max(info[flower][3], query[3])]
        print(0 if query==False else(query[1]-query[0]+query[3]-query[2]+2)*2)
# Passed 60%
# [PP][PP]PPPP-TT[TT]