class Solution:
    def compute(self, n, k):
        # write your code here
        MOD = 10**9 +7
        
        if n<2:
            return 0
        
        N=n-2
        
        fact = [1]*(N+1)
        inverse_fact=[1]*(N+1)
        
        for i in range(1,N+1):
            fact[i]=(fact[i-1]*i)%MOD
            
        inverse_fact[N]=pow(fact[N],MOD-2,MOD)
        
        for i in range(N-1,-1,-1):
            inverse_fact[i]=(inverse_fact[i+1]*(i+1))%MOD
            
        def nCr(n,r):
            if r<0 or r>n:
                return 0
            
            num=fact[n]
            den=(inverse_fact[r]*inverse_fact[n-r])%MOD
            return (num*den)%MOD
        
        if k==0:
            return 0
            
        k1=(k-1)//2
        k2=k//2

        if k%2==1:
            comb=nCr(N,k1)
            result=(2*comb*comb)%MOD
        else:
            comb1=nCr(N,k1)
            comb2=nCr(N,k2)
            result=(2*comb1*comb2)%MOD
        
        return result
            