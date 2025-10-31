class Solution {
public:
    bool checkIfPangram(string sentence) {
        sort(sentence.begin(),sentence.end());
            int alp='a',count=0;
        for(int i=0;i<sentence.length();i++){
            if(sentence[i]==alp && alp!=('z'+1)){
                count++;
                alp++;
            }
        }
        if(count==26)
            return true;
        else
            return false;
    }
};