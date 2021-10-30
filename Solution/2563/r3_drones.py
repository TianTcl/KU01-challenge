# import math
# d_count, d_dest, d_dist, sv_dc, sv_ed = int(input()), [int(a) for a in input().split()], 0, 1, list(())
# d_dest.sort(reverse=True)
# for e_itr in range(math.ceil(d_count/10)):
#     e_nl = d_dest[e_itr*10+math.ceil(d_count/10):((e_itr+1)*10 if (e_itr+1)*10<=d_count-math.ceil(d_count/10) else d_count)+math.ceil(d_count/10)-1]
#     e_nl.sort()
#     e_nl.append(d_dest[e_itr])
#     sv_ed.append(e_nl)
# for e_ds in sv_ed:
#     for e_ind, e_dist in enumerate(e_ds):
#         d_dist += e_dist*sv_dc*(1 if e_ind==len(e_ds)-1 else 2)
#     sv_dc += 1
# print(d_dist) #+(1 if math.ceil(d_count/10)>1 else 0)
# Passed
# 10% Unknown code error

# import math
# d_count, d_dest, d_dist, sv_dc, sv_ed = int(input()), [int(a) for a in input().split()], 0, 1, list(())
# d_dest.sort(reverse=True)
# d_drones = d_dest[math.ceil(d_count/10):]
# for e_itr in range(math.ceil(d_count/10)):
#     e_nl = d_drones[e_itr*9:(e_itr+1)*10-1]
#     e_nl.append(d_dest[e_itr])
#     sv_ed.append(e_nl)
# for e_ds in sv_ed:
#     for e_ind, e_dist in enumerate(e_ds):
#         d_dist += e_dist*sv_dc*(1 if e_ind==len(e_ds)-1 else 2)
#     sv_dc += 1
# print(d_dist-(1 if math.ceil(d_count/10)>1 else 0))
# Passed
# 10% Unknown code error