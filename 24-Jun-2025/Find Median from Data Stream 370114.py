# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.min_ = []
        self.max_ = []

    def addNum(self, num: int) -> None:
        heappush(self.max_, -num)
        a = -heappop(self.max_)
        heappush(self.min_, a)
        if len(self.min_) > len(self.max_):
            b = -heappop(self.min_)
            heappush(self.max_, b)

        

    def findMedian(self) -> float:
        if len(self.max_) > len(self.min_):
            return -self.max_[0]
        else:
            return (self.min_[0] + -self.max_[0])/2
        


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()