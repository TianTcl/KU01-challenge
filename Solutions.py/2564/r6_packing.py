# [ifo_maxX, ifo_maxY, ifo_minX, ifo_minY] = [int(a) for a in input().split()]
# ifo_size = max({ifo_maxX//each_size for each_size in range(ifo_minX, ifo_minY + 1)}.union({ifo_maxY//each_size for each_size in range(ifo_minX, ifo_minY + 1)}))
# amt_used = ifo_size * (ifo_maxX if "check side" else ifo_maxY)

[ifo_maxX, ifo_maxY, ifo_minX, ifo_minY] = [int(a) for a in input().split()]
print(min([(ifo_maxX % each_size) * (ifo_maxY % each_size) for each_size in range(ifo_minX, ifo_minY + 1)]))
# Passed
# 100%
