class Solution {
public:
    int minPartitions(string n) {
        int a=0;
        for(int i=0;i<n.length();i++)
            if(n[i]>a)
                a=n[i];
        
        return a-'0';                    
    }
};