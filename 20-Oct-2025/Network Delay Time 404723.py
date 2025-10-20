# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        time = {i:float('inf') for i in range(1, n + 1)}
        time[k] = 0
        heap = [(0, k)]

        while heap:
            cost, curr = heappop(heap)

            for child, t in graph[curr]:
                new = t + cost
                if new < time[child]:
                    time[child] = new
                    heappush(heap, (new, child))
        ans = max(time.values())

        return ans if ans != float('inf') else -1
        