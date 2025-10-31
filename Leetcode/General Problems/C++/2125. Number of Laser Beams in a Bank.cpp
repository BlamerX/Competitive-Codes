class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int n=bank.size(),m=bank[0].size(),cnt=0,sum=0;
        for(int i=0;i<n;i++){
            int one=0;
            for(int j=0;j<m;j++){
                if(bank[i][j]=='1')
                    one++;
            }
            if(one!=0)
                sum+=one*cnt;
            else
                continue;
            cnt=one;
        }
        return sum;
    }
};