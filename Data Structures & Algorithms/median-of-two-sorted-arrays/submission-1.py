class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m - 1  # binary search bounds on nums1

        while True:
            i = (l + r) // 2 if m > 0 else -1   # partition index for nums1
            j = half - i - 2                     # partition index for nums2

            left1 = nums1[i] if i >= 0 else float('-infinity')
            right1 = nums1[i + 1] if (i + 1) < m else float('infinity')
            left2 = nums2[j] if j >= 0 else float('-infinity')
            right2 = nums2[j + 1] if (j + 1) < n else float('infinity')

            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1