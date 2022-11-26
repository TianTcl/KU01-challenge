station, path1, path2, cross = int(input()), [int(_) for _ in ("1 "+input()).split()], [int(_) for _ in ("1 "+input()).split()], 0
untrue = (1, station-1)
for stop in range(station):
    sameStation = len({path1[stop],path2[stop],path1[stop+1],path2[stop+1]})
    if sameStation==2: cross += 1
    elif (abs(path1[stop]-path1[stop+1]) in untrue or abs(path2[stop]-path2[stop+1]) in untrue or sameStation==3): continue
    side = range(min(path1[stop], path1[stop+1])+1, max(path1[stop], path1[stop+1]))
    if (int(path2[stop] in side) ^ int(path2[stop+1] in side)): cross += 1
print(cross)
# Passed