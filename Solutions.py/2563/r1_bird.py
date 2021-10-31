tree_count, tree_hinput, tree_chosen = int(input()), input().split(), 0
tree_height = [int(x) for x in tree_hinput]
for each_tree in range(tree_count):
    if each_tree==0 and tree_height[0]>tree_height[1]:tree_chosen+=1
    elif each_tree==tree_count-1 and tree_height[each_tree]>tree_height[each_tree-1]:tree_chosen+=1
    elif tree_height[each_tree-1]<tree_height[each_tree]>tree_height[each_tree+1]:tree_chosen+=1
print(tree_chosen)
# Passed