class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dp = [[[-1 for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == -1:
                        continue
                        
                    current_score = dp[i][j][c]

                    if j + 1 < n:
                        val = grid[i][j+1]
                        cell_score = val
                        cell_cost = 1 if val > 0 else 0
                        
                        new_total_cost = c + cell_cost
                        new_total_score = current_score + cell_score
                        
                        if new_total_cost <= k:
                            dp[i][j+1][new_total_cost] = max(
                                dp[i][j+1][new_total_cost], 
                                new_total_score
                            )
                            
                    if i + 1 < m:
                        val = grid[i+1][j]
                        
                        cell_score = val
                        cell_cost = 1 if val > 0 else 0
                        
                        new_total_cost = c + cell_cost
                        new_total_score = current_score + cell_score
                        
                        if new_total_cost <= k:
                            dp[i+1][j][new_total_cost] = max(
                                dp[i+1][j][new_total_cost], 
                                new_total_score
                            )

        final_max_score = max(dp[m-1][n-1])
        
        return final_max_score