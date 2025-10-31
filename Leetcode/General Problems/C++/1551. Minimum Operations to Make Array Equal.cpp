class Solution {
public:
    int minOperations(int n) {
        int arr[n],sum=0;
        for(int i=0;i<n;i++)
            arr[i]=(2*i)+1;
        
        if(n%2==0){
            int eq=arr[n/2-1]+1;
            for(int i=0;i<n/2;i++)
                sum+=eq-arr[i];            
        }
        else{
            int eq=arr[n/2];
            for(int i=0;i<n/2;i++)
                sum+=eq-arr[i];
        }
        return sum;
    }
};