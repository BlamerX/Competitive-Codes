from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        small=min(nums)
        large=max(nums)

        completeSet=set(range(small,large+1))
        givenSet=set(nums)
        return sorted(list(completeSet-givenSet))
    
if __name__ == "__main__":
    solution_tester = Solution()

    user_input = input()

    nums = [int(num) for num in user_input.split()]
        
    missing = solution_tester.findMissingElements(nums)
    print(missing)