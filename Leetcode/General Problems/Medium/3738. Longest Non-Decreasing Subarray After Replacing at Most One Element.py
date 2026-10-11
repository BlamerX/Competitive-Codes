from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return n

        left = [1] * n
        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                left[i] = left[i-1] + 1

        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1] + 1

        max_len = 0
        for length in left:
            max_len = max(max_len, length)

        for i in range(n):
            if i > 0 and i < n - 1:
                if nums[i-1] <= nums[i+1]:
                    max_len = max(max_len, left[i-1] + 1 + right[i+1])
            
            if i > 0:
                max_len = max(max_len, left[i-1] + 1)

            if i < n - 1:
                max_len = max(max_len, right[i+1] + 1)
                
        return max_len
