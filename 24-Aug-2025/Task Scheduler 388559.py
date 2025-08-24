# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        check = Counter(tasks)
        c = max(check.values())
        return max(len(tasks),(c- 1) * (n + 1) + sum(1 for v in check.values() if v == c))