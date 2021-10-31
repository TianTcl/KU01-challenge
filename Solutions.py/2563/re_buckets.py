# bucket_counts, bucket_input, bucket_export = [int(a) for a in input().split()], list(()), set(())
# for each_bin in range(bucket_counts[0]): bucket_input.append([int(b) for b in input().split()])
# for bucket_output in [int(c)-1 for c in input().split()]:
#     for each_bucket in range(bucket_counts[0]):
#         if each_bucket!=bucket_output and bucket_input[bucket_output][0]>bucket_input[each_bucket][0] and bucket_input[bucket_output][1]<bucket_input[each_bucket][1]:
#             bucket_export.add(each_bucket if bucket_input[bucket_output][0]>bucket_input[each_bucket][0] and bucket_input[bucket_output][1]<bucket_input[each_bucket][1] else bucket_output)
#             break
# print(len(bucket_export))
# for each_cout in sorted(list(bucket_export)[:-1]): print(each_cout+1, end=" ")
# print(sorted(list(bucket_export))[-1])

bucket_counts, bucket_input, bucket_info = [int(a) for a in input().split()], list(()), dict()
for each_bin in range(bucket_counts[0]): bucket_input.append([int(b) for b in input().split()])
bucket_require, bucket_contain, bucket_passed = [int(c)-1 for c in input().split()], list(()), list(())
for each_nb in range(bucket_counts[0]): bucket_info[each_nb] = [each_nb]
for each_bucket in range(bucket_counts[0]):
    for each_inside in bucket_require:
        if each_bucket!=each_inside and bucket_input[each_bucket][0]<bucket_input[each_inside][0] and bucket_input[each_bucket][1]>bucket_input[each_inside][1]:
            if each_bucket in bucket_info: bucket_info[each_bucket].append(each_inside)
            else: bucket_info[each_bucket] = [each_inside]
for each_keys in bucket_info.keys():
    each_count = 0
    for each_require in bucket_require:
        if each_require in bucket_info[each_keys]: each_count += 1
    if each_count > 0: bucket_contain.append([each_keys, each_count, len(bucket_info[each_keys])-each_count])
def find_most():
    bucket_cc, bucket_ck, bucket_cw = 0, 0, len(bucket_input)
    for each_contain in bucket_contain:
        if (each_contain[1] > bucket_cc and each_contain[2] <= bucket_cw) or (each_contain[1] >= bucket_cc and each_contain[2] < bucket_cw):
            bucket_cc, bucket_ck, bucket_cw = each_contain[1], each_contain[0], each_contain[2]
    bucket_contain.remove([bucket_ck,bucket_cc,bucket_cw])
    bucket_passed.append(bucket_ck)
    return bucket_cc
def find_all(bucket_left):
    bucket_chosed = find_most()
    if bucket_chosed>=bucket_left:
        print(len(bucket_passed))
        for each_chosen in [int(d)+1 for d in sorted(bucket_passed)]: print(each_chosen, end=" ")
    else:
        bucket_left -= bucket_chosed
        find_all(bucket_left)
find_all(len(bucket_require))
# Failed
# waste bucket error