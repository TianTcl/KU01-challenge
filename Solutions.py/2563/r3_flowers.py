uin, sv_dr = [int(a) for a in input().split()], 0
while sv_dr*(sv_dr+1)/2<uin[1]: sv_dr += 1
print(sv_dr//uin[0]+(0 if sv_dr%uin[0]==0 else 1))
# Passed