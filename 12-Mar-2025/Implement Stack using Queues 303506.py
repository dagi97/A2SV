# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.Stack = deque()
        

    def push(self, x: int) -> None:
        self.Stack.append(x)

        

    def pop(self) -> int:
        return self.Stack.pop()

    def top(self) -> int:
       return self.Stack[-1]
        

    def empty(self) -> bool:
        return not self.Stack
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()