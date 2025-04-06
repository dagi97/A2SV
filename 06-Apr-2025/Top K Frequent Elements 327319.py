# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = Counter(nums)
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        for key,val in mydict.items():
            bucket[val].append(key)
       
        res = []
        for i in range(len(bucket)-1,-1,-1):
            if len(res) == k:
                break
            res.extend(bucket[i])
        return res
         

        