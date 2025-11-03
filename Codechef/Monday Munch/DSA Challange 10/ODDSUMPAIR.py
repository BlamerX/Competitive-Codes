class Solution:
    def check_odd_pairs(self, a, b, c):
        # write your code here
        even = (a%2==0) and (b%2==0) and (c%2==0)
        odd = (a%2!=0) and (b%2!=0) and (c%2!=0)
        
        if even or odd:
            return "NO"
        else:
            return "YES"
