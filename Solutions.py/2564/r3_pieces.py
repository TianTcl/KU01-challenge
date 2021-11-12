[size_x, size_y, amt_cutX, amt_cutY, amt_ask], ifo_cut, tmp_size, ifo_size = [int(a) for a in input().split()], list(()), 0, list(())
for each_cutX in sorted([int(b) for b in (input()+" "+str(size_x)).split()]):
    ifo_cut.append(each_cutX - tmp_size)
    tmp_size = each_cutX
tmp_size = 0
del size_x
for each_cutY in sorted([int(c) for c in (input()+" "+str(size_y)).split()]):
    for each_size in ifo_cut: ifo_size.append((each_cutY - tmp_size) * each_size)
    tmp_size = each_cutY
del ifo_cut, size_y
for each_ask in range(amt_ask): print(ifo_size.count(int(input())))
# Passed
# 20% [ PPT[xx][xx][xx][xx][xx][xx][xx] ]