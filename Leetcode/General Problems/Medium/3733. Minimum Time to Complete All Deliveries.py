from typing import List
import math

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        nums = [d, r]
        
        d1, d2 = nums[0][0], nums[0][1]
        r1, r2 = nums[1][0], nums[1][1]
        
        def gcd(a, b):
            return math.gcd(a, b)

        def check(T: int) -> bool:
            g = gcd(r1, r2)
            lcm = (r1 // g) * r2
            slots1 = (T // r2) - (T // lcm)
            slots2 = (T // r1) - (T // lcm)
            common_slots = T - (T // r1) - (T // r2) + (T // lcm)
            d1_needs = max(0, d1 - slots1)
            d2_needs = max(0, d2 - slots2)
            return (d1_needs + d2_needs) <= common_slots
        
        low = 1 
        high = 2 * (d1 + d2)
        output = high

        while low <= high:
            mid = (low + high) // 2
            
            if check(mid):
                output = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return output

if __name__ == "__main__":
    solution_tester = Solution()
    
    d1 = int(input())
    d2 = int(input())
        
    r1 = int(input())
    r2 = int(input())
        
    d_input = [d1, d2]
    r_input = [r1, r2]
        
    min_time = solution_tester.minimumTime(d_input, r_input)

    print(min_time)