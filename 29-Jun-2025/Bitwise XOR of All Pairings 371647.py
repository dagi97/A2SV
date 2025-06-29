# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a = len(nums1)
        b = len(nums2)
        x, y = 0, 0
        if a % 2:
            for i in nums2:
                x ^= i
        if b % 2:
            for i in nums1:
                y ^= i
        return x ^ y

     

        