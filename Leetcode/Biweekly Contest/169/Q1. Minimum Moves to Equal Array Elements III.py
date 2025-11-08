class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves=0
        for num in nums:
            moves+=(max(nums)-num)

        return moves