class Solution {
public:
    int sum(int start,int end){
        int sum=0;
        for(int i=start;i<=end;i++){
            sum+=i;
        }
        return sum;
    }
    int pivotInteger(int n) {
        int pivot=-1;

        if(n==1)
            return 1;
            
        for(int i=1;i<n;i++){
            if(sum(1,i)==sum(i,n))
                pivot=i;
        }

        return pivot;
    }
};