class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        def count_less_equal(mid):
            count = 0
            row, col = 0, n - 1
            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    count += col + 1 
                    row += 1
                else:
                    col -= 1
            return count
        
        while low < high:
            mid = (low + high) // 2
            cnt = count_less_equal(mid)
            if cnt < k:
                low = mid + 1
            else:
                high = mid
        return low