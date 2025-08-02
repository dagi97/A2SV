# Problem: Number of Nodes in the Sub-Tree With the Same Label - https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution:
    def countSubTrees(self, n, edges, labels):
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        ans = [0] * n

        def dfs(node, parent):
            count = Counter()
            label = labels[node]
            count[label] += 1

            for child in tree[node]:
                if child == parent:
                    continue
                child_count = dfs(child, node)
                count += child_count

            ans[node] = count[label]
            return count

        dfs(0, -1)
        return ans