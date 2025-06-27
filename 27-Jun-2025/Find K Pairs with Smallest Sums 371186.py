# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for i in range(min(k, len(nums1))):
            heappush(h, (nums1[i] + nums2[0], i, 0))
        res = []
        while h and len(res) < k:
                s, i, j =heappop(h)
                res.append([nums1[i], nums2[j]])
                if j + 1 < len(nums2):
                    
                    heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return res