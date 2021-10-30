# rin, kn_x, kn_y = input().split(), input().split(), input().split()
# def s(kn_t, axis):
#     b_s = list(())
#     for e_i, e_v in enumerate([int(a) for a in kn_t]):
#         if e_i==0: b_s.append(e_v)
#         elif e_i==len(kn_t)-1: b_s.append(int(rin[axis])-e_v)
#         else: b_s.append(e_v-int(kn_t[e_i-1]))
#     b_s.sort(reverse=True)
#     return [b_s[0], b_s[1]]
# b_sx, b_sy = s(kn_x, 0), s(kn_y, 1)
# b_c = [b_sx[0]*b_sy[0], b_sx[0]*b_sy[1], b_sx[1]*b_sy[0], b_sx[1]*b_sy[1]]
# b_c.sort(reverse=True)
# print(b_c[0], b_c[1])
# Passed
# 75% unknown error

rin, kn_x, kn_y, areas = [int(a) for a in input().split()], [0], [0], list(())
kn_x.extend([int(b) for b in input().split()])
kn_y.extend([int(c) for c in input().split()])
kn_x.append(rin[0])
kn_y.append(rin[1])
for ex in range(1,len(kn_x)):
    for ey in range(1,len(kn_y)): areas.append((kn_x[ex]-kn_x[ex-1])*(kn_y[ey]-kn_y[ey-1]))
areas.sort(reverse=True)
print(areas[0], areas[1])
# Passed