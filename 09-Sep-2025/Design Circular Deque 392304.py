# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.c = k
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.c  != 0:
            self.q.appendleft(value)
            self.c -= 1
            return True
        return False
        
        

    def insertLast(self, value: int) -> bool:
        if self.c  != 0:
                self.q.append(value)
                self.c -= 1
                return True
        return False
        

    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft()
            self.c += 1
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            self.c += 1
            return True
        return False
        

    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        return -1 
        

    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        return -1 
        

    def isEmpty(self) -> bool:
        return not self.q
        

    def isFull(self) -> bool:
        return self.c  == 0
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()