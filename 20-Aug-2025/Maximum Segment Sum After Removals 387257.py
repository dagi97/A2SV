# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = list(range(n))
        seg_sum = [0] * n
        active = [False] * n
        res = [0] * n
        max_sum = 0

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            nonlocal max_sum
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
                seg_sum[rx] += seg_sum[ry]
                max_sum = max(max_sum, seg_sum[rx])

        for i in range(n - 1, -1, -1):
            res[i] = max_sum
            idx = removeQueries[i]
            active[idx] = True
            parent[idx] = idx
            seg_sum[idx] = nums[idx]
            max_sum = max(max_sum, nums[idx])

            if idx > 0 and active[idx - 1]:
                union(idx, idx - 1)
            if idx < n - 1 and active[idx + 1]:
                union(idx, idx + 1)

        return res
