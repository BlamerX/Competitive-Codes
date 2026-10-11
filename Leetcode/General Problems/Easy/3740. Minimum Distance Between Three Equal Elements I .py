class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        min_dist = float('inf')
        
       
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                        
                    if nums[i] == nums[j] and nums[j] == nums[k]:
                        
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        
                        min_dist = min(min_dist, dist)

        if min_dist == float('inf'):
            return -1
        else:
            return min_dist