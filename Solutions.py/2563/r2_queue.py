uin, eh, ih, mh = input().split(), [int(a) for a in input().split()], input().split(), 0
for eidx, efnd in enumerate(eh):
    if str(eidx+1) in ih:
        if eidx==0:
            print(0)
            mh=efnd
        else:
            print(0 if efnd>mh else mh-efnd+1)
    mh=max(mh,efnd if efnd>mh else mh-efnd+1)
# Passed