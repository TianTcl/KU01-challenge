[amt_ppl, amt_skip, ifo_theif], amt_parse, ifo_now = [int(a) for a in input().split()], 0, 1
while not ((ifo_now == 1 or ifo_now == ifo_theif) and amt_parse > 0):
    ifo_now, amt_parse = ifo_now + amt_skip, amt_parse + 1
    if ifo_now > amt_ppl: ifo_now -= amt_ppl
print(amt_parse + (1 if ifo_now == ifo_theif else 0))
# Passed
# 30% (- เจ็ดอัน)