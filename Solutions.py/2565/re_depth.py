[levels, ships], shape, level, deepest = [int(_) for _ in input().split()], [], 0, 0
# Canal converter
for _ in range(levels):
    layer = [int(_) for _ in input().split()]
    level += layer[0]
    if layer[0]==-1:
        shape[level].append(0)
    elif level>deepest:
        shape.append([0])
        deepest += 1
    for diff in range(level):
        shape[diff][-1] += layer[1]
# Optimize maximimum length
for _ in range(deepest):
    shape[_] = max(shape[_])
# Ship testment
for _ in range(ships):
    size, printed = int(input()), False
    # print(len(list(filter(lambda level: level>=size, shape))))
    for layer in range(deepest):
        if size>shape[layer]:
            print(layer)
            printed = True
            break
    if not printed: print(deepest)
# Passed 30%
# T = 7