penguins, lane, crosses = int(input()), [], 0
for _ in range(penguins): lane.append(int(input()))
for path1, slide1 in enumerate(lane):
    for path2, slide2 in enumerate(lane):
        if path2>path1 and slide1<slide2: crosses += 1
print(crosses)
# Passed