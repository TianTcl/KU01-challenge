#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

struct Pair {
    int min;
    int max;
};

struct Tree {
    int number;
    Pair size;
    vector<int> child;
};

int main() {
    int n,m; cin >> n >> m;
        vector<Tree> tree;
    for (int i=0; i < n ; i++) {
        Pair tmp;
        cin >> tmp.min >> tmp.max;
        Tree tree_tmp;
        tree_tmp.number = i;
        tree_tmp.size = tmp;
        tree_tmp.child = vector<int>();
        for (int j=0;j<tree.size();j++) {
            if (tmp.min > tree[j].size.min && tree[j].size.max > tmp.max) {
                tree[j].child.push_back(i);
            }
        }
        tree.push_back(tree_tmp);
    }
    
}
