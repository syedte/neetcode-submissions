class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        mid = n // 2
        if n % 2== 0:
            return (self.nums[mid] + self.nums[mid - 1]) / 2
        else:
            return float(self.nums[mid])

        
        