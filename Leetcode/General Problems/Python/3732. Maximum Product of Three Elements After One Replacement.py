from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort() 
        
        R = 100000

        prod = max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )
        max_prod = max(
            nums[-1] * nums[-2],  
            nums[0] * nums[1]
        )
        prod_with_R = R * max_prod

        min_prod = nums[0] * nums[-1]
        prod_with_neg_R = -R * min_prod
        
        return max(prod, prod_with_R, prod_with_neg_R)

if __name__ == "__main__":
    solution_tester = Solution()
    
    user_input = input()

    nums = [int(num) for num in user_input.split()]
    
    max_prod = solution_tester.maxProduct(nums)
    print(max_prod)