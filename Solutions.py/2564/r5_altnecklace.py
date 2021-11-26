[amt_bead, amt_swap, amt_isrt], ifo_swap = [int(a) for a in input().split()], list(())
for each_swap in range(amt_swap): ifo_swap.append(int(input()) - 1)
ifo_swap.append(amt_bead - 1)
for each_isrt in range(amt_isrt):
    [ifo_pos, ifo_col], tmp_pos = [int(b) for b in input().split()], 0
    ifo_pos -= 1
    while ifo_pos > ifo_swap[tmp_pos]: tmp_pos += 1
    if ifo_col == abs((tmp_pos % 2) - 1): pass
    elif ifo_pos + 1 == ifo_swap[tmp_pos]: pass
    elif ifo_pos - 1 >= ifo_swap[tmp_pos]:
        ifo_swap.insert(tmp_pos, ifo_pos)
        if ifo_pos + 1 < ifo_swap[tmp_pos]: ifo_swap.insert(tmp_pos + 1, ifo_pos + 1)
print(len(ifo_swap))