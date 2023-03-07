spInput = lambda : [int(_) for _ in input().split()]
[factory, items], time2Q, time2F, most = spInput(), [spInput(), spInput()], [spInput(), spInput()], set()
time2Q[0].sort()
time2Q[1].sort()
time2F[0].sort()
time2F[1].sort()
for test in range(factory+1):
    if items-test>factory: continue
    tempt2Q, tempt2F, time2T = [time2Q[0][:test], time2Q[1][:items-test]], [time2F[0][:test], time2F[1][:items-test]], []
    tempt2F[0].sort(reverse=True)
    tempt2F[1].sort(reverse=True)
    for package in range(test): time2T.append(tempt2Q[0][package]+tempt2F[0][package])
    for package in range(items-test): time2T.append(tempt2Q[1][package]+tempt2F[1][package])
    time2T.sort()
    most.add(time2T[items-1])
print(min(most))
# Passed