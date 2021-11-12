amt_ppl, ifo_parse, amt_round = int(input()), dict(()), 0
ifo_now, ifo_done = [a for a in range(amt_ppl)], [False for b in range(amt_ppl)]
for each_ifo in range(amt_ppl): ifo_parse[each_ifo] = int(input()) - 1
while ifo_done.count(True) < amt_ppl:
    amt_round, tmp_ifo = amt_round + 1, ifo_now.copy()
    for each_ppl in range(amt_ppl):
        ifo_now[ifo_parse[each_ppl]] = tmp_ifo[each_ppl]
        if ifo_now[each_ppl] == each_ppl and not ifo_done[each_ppl]: ifo_done[each_ppl] = True
print(amt_round)
# Passed
# 60% (T สี่อัน)