# amt_bowl, amt_size, amt_stack = int(input()), list(()), 0
# for each_bowl in range(amt_bowl): amt_size.append(int(input()))
# amt_max = sorted(amt_size)[-1]
# def new_stack():
#     global amt_size, amt_stack
#     amt_size.sort()
#     amt_min = 0
#     for each_bowl in amt_size.copy():
#         if each_bowl > amt_min:
#             amt_size.remove(each_bowl)
#             amt_min = each_bowl
#     amt_stack += 1
#     if len(amt_size) > 0: new_stack()
# new_stack()
# print(amt_stack)
# Passed
# 60% (T สี่กรณี)

# amt_bowl, amt_size, amt_max = int(input()), list(()), 1
# for each_bowl in range(amt_bowl): amt_size.append(int(input()))
# last_bowl, last_stack = sorted(amt_size)[0], 1
# for each_size in sorted(amt_size):
#     if each_size == last_bowl: last_stack += 1
#     else:
#         amt_max = max(last_stack, amt_max)
#         last_bowl, last_stack = each_size, 1
# print(amt_max)
# Passed
# 100%

amt_bowl, amt_size = int(input()), list(())
for each_bowl in range(amt_bowl): amt_size.append(int(input()))
print(max([amt_size.count(each_size) for each_size in set(amt_size)]))
# Passed
# 100%