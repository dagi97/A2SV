# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(stones)):
            for j in range(i + 1 ,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()

        def dfs(i):
            visited.add(i)
            for n in graph[i]:
                if n not in visited:
                    dfs(n)
        component = 0
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                component += 1

        return len(stones) - component





      
        