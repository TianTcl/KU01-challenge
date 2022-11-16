[logs, length, move], holes, possible = [int(_) for _ in input().split()], [], False
for _ in range(logs): holes.append(list(map(int, input().split()))[1:])
# Compare changing main log
for layer, main in enumerate(holes):
    through = True
    # Compare each layer
    for test, drills in enumerate(holes):
        if not through: break
        elif layer!=test:
            # Compare 2 logs
            passed = False
            for source in main:
                for drill in drills:
                    if abs(drill-source)<=move:
                        passed = True
                        break
                if passed: break
            through &= passed
    if through:
        possible = True
        break
print(1 if possible else 0)
# Failed
# 0: [-P][-P][-P-][--P][P--][PTPT-][--PPP--][T-PP][-PTP][P-TTT]