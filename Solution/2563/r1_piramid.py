uin, sos, oll, ioc = input().split(), lambda n : n*(n+1)*(2*n+1)/6, 0, 0
orange_count = sos(int(uin[0]))-int(uin[1])
for run in range(int(uin[0])):
    if ioc>=orange_count: break
    ioc+=(int(uin[0])-run)**2
    oll+=1
print(oll)
# Passed