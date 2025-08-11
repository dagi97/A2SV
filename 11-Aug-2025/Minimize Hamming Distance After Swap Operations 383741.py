# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            parent[find(a)] = find(b)
        
        for a, b in allowedSwaps:
            union(a, b)
        
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        distance = 0
        for indices in groups.values():
            src_count = {}
            tgt_count = {}
            for i in indices:
                src_count[source[i]] = src_count.get(source[i], 0) + 1
                tgt_count[target[i]] = tgt_count.get(target[i], 0) + 1
            for val, cnt in tgt_count.items():
                if val in src_count:
                    match = min(src_count[val], cnt)
                    src_count[val] -= match
            distance += sum(src_count.values())
        
        return distance
