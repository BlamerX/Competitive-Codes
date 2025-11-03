class Solution:
    def check_array(self, A):
        # write your code here 
        total_sum=sum(A)
        
        if total_sum%2!=0:
            return "NO"
        else:
            return "YES"