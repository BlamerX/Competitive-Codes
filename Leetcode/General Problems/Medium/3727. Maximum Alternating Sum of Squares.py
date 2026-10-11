class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        square = [x * x for x in nums]
        sorted_square = sorted(square)
        k = len(nums) // 2
        small_sum = sum(sorted_square[:k])
        total = sum(square)
        return total - 2 * small_sum