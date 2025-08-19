# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        heap = []
        t = tasks[0][0]
        i = 0
       
        while heap or  i < len(tasks):

            while i < len(tasks) and tasks[i][0] <= t:
                val = tasks[i]
                heappush(heap, [val[1],val[2]])
                i += 1
            if not heap:
                t = tasks[i][0]
            else:
                a, b = heappop(heap)
                ans.append(b)
                t += a
        return ans
            

            
        


        

       

        