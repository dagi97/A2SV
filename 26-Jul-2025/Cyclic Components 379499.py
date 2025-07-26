# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict, deque


n,e = map(int, input().split())
graph = defaultdict(list)
visited =  set()
c = 0

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
      
def bfs(start):
    queue = deque([start])
    visited.add(start)
    flag = True
    while queue:
        node = queue.popleft()
        if len(graph[node]) != 2:
            flag = False   
        for nei in graph[node]:
            if  nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return flag

for node in range(1, n + 1):
    if node not in visited:
        if bfs(node):
            c += 1

print(c)
