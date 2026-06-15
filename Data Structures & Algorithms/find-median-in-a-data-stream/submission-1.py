class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # always push the first num to small 
        heapq.heappush(self.small, -num)
        # before pushing the other element let us check if its > or < of small 
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # we check the size of heaps 
        if len(self.small) > len(self.large) + 1:
            # small is allowed to have 1 extra element
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        return ( -self.small[0] + self.large[0]) / 2
        
        