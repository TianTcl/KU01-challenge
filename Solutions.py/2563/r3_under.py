uin, tdata, umax = [int(a) for a in input().split()], list(()), 0
for et in range(uin[1]): tdata.append([int(b) for b in input().split()])
for ep in range(uin[0]):
    tmax = 0
    for et in tdata:
        if ep>et[0] and ep<=et[1]: tmax += 1
    umax = max(tmax, umax)
print(umax)
# Passed