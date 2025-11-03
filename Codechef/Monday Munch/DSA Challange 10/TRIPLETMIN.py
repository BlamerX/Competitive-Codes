from bisect import bisect_left

class Solution:
    def process_queries(self, a: list[int], queries: list[int]) -> list[int]:
        # write your code here 
        n=len(a)
        
        a.sort()
        
        total_counts=[]
        current_total=0
        
        for i in  range(n-2):
            m=n-1-i
            
            count=(m*(m-1))//2
            current_total+=count
            total_counts.append(current_total)
        
        results=[]
        
        for k in queries:
            index=bisect_left(total_counts,k)
            results.append(a[index])
            
        return results
