# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        check = [0]* len(nums1)
        for i in range(len(nums1)):
            check[i] = nums1[i] - nums2[i]
        

        print(check)
        count = 0
        def merge_sort(l, r):
            if l >= r:
                return 0
            
            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid + 1, r)
          
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and check[i] > check[j] + diff:
                    j += 1
                count += (r - j + 1)   
            
           
            temp = []
            p1, p2 = l, mid + 1
            while p1 <= mid and p2 <= r:
                if check[p1] <= check[p2]:
                    temp.append(check[p1])
                    p1 += 1
                else:
                    temp.append(check[p2])
                    p2 += 1
            while p1 <= mid:
                temp.append(check[p1])
                p1 += 1
            while p2 <= r:
                temp.append(check[p2])
                p2 += 1
            
            check[l:r+1] = temp
            return count
        
        return merge_sort(0, len(check) - 1)

        