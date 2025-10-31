class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {

        int c=0;
        for(auto &i:jewels){
            for(auto &j:stones){
                if(i==j)
                    c++;
            }
        }
        return c;
        
    }
};