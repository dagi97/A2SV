# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
       
        graph = defaultdict(list)
        c = 0
        
        
        for u, v in edges:
            p = succProb[c]
            graph[u].append((v,p))
            graph[v].append((u, p))
            c += 1
        
        heap = []
        heappush(heap, [-1, start_node, -1])
        


        while heap:
            prob, node, parent = heappop(heap)
            prob *= -1

            if node == end_node:
                return prob

            for nei, p in graph[node]:
                if nei != parent:
                    new_prob = p * prob
                    new_prob *= -1
                    heappush(heap, [new_prob, nei, node])
        return 0
      





