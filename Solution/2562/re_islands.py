init_info = input().split(" ")
ws_width = int(init_info[0])
ws_li = int(init_info[1])
ws_input = input().split(" ")
ws_level = []
for each_place in ws_input:
    ws_level.append(int(each_place))

maxs = 0
alls = []
for each_pos in ws_level:
    if each_pos < 1:
        alls.append(1-each_pos)
alls.sort()
for eachs in range(round(len(alls)*4/5)):
    maxs += alls[eachs]
sets = set((alls))
news = list((sets))
import random
print(random.randint(alls[0],news[round(len(news)*4/5)]))
    #Stopped