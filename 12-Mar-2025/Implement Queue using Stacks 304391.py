# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        self.ind = 0
      
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        

    def pop(self) -> int:
        c = self.stack[self.ind]
        self.ind += 1
        return c

    def peek(self) -> int:
        return self.stack[self.ind]
        

    def empty(self) -> bool:
        return len(self.stack) - self.ind == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()