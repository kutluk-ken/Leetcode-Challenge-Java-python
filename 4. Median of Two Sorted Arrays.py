class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0
        m, n = len(nums1), len(nums2)

        def get_min():
            nonlocal p1,p2

            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1+=1
                else:
                    ans = nums2[p2]
                    p2+=1
            elif p2 == n:
                ans = nums1[p1]
                p1+=1
            else:
                ans = nums2[p2]
                p2+=1
            return ans

        if (m+n)%2 == 0:
            for _ in range((m+n)//2-1):
                _ = get_min()
            return (get_min() + get_min())/2
        else:
            for _ in range((m+n)//2):
                _ = get_min()
            return get_min()
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.*/
