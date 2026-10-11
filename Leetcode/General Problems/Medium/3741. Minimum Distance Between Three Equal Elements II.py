from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
            
        min_dist = float('inf')

        for indices in positions.values():
            if len(indices) < 3:
                continue

            for i in range(len(indices) - 2):
                idx_min = indices[i]
                idx_max = indices[i+2]
                
                dist = 2 * (idx_max - idx_min)
                min_dist = min(min_dist, dist)
        
        if min_dist == float('inf'):
            return -1
        else:
            return min_dist