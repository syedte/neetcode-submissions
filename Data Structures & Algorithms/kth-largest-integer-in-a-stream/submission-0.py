class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)  # sort descending
        return self.nums[self.k - 1]       # kth largest