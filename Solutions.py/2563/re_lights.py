pillar_count, pillar_info, total_dist, total_answer = int(input()), list(()), 0, 0
for each_pin in range(pillar_count): pillar_info.append(int(input()))
for each_pillar in sorted(pillar_info):
    total_dist += each_pillar
    total_answer += total_dist*2
print(total_answer)
# Passed
# 100%