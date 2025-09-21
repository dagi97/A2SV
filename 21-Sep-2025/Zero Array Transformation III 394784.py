# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums, queries):
        n = len(nums)
        queries.sort()
        d = [0] * (n + 1)
        heap = []
        def push(x):
            heap.append(x)
            i = len(heap) - 1
            while i > 0:
                p = (i - 1) // 2
                if heap[p] < heap[i]:
                    heap[p], heap[i] = heap[i], heap[p]
                    i = p
                else:
                    break
        def pop():
            if not heap:
                return None
            res = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                i = 0
                N = len(heap)
                while True:
                    l = 2 * i + 1
                    r = l + 1
                    largest = i
                    if l < N and heap[l] > heap[largest]:
                        largest = l
                    if r < N and heap[r] > heap[largest]:
                        largest = r
                    if largest == i:
                        break
                    heap[i], heap[largest] = heap[largest], heap[i]
                    i = largest
            return res
        def top():
            return heap[0] if heap else -10**18
        s = 0
        j = 0
        m = len(queries)
        for i in range(n):
            s += d[i]
            while j < m and queries[j][0] <= i:
                push(queries[j][1])
                j += 1
            while s < nums[i] and heap and top() >= i:
                s += 1
                end = pop()
                d[end + 1] -= 1
            if s < nums[i]:
                return -1
        return len(heap)
