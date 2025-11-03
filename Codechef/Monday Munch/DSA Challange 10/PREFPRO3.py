class Solution:
    def count_subarrays_with_sum_k(self, arr, k):
        # write your code here 
        prefex_sums={0:1}
        
        current_sum=0
        total_count=0
        
        for num in arr:
            current_sum+=num
            
            complement=current_sum-k
            
            if complement in prefex_sums:
                total_count+=prefex_sums[complement]
            
            if current_sum in prefex_sums:
                total_count+=prefex_sums[complement]
            
            if current_sum in prefex_sums:
                prefex_sums[current_sum]+=1
            else:
                prefex_sums[current_sum]=1
        
        return total_count