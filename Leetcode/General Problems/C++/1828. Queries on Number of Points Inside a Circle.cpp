class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        int psize=points.size(),qsize=queries.size();
        vector<int> answer;
        for(int i=0;i<qsize;i++){
            int cnt=0;
            for(int j=0;j<psize;j++){
                if((sqrt(pow(points[j][0]-queries[i][0],2)+pow(points[j][1]-queries[i][1],2)))<=queries[i][2])
                    cnt++;
            }
            answer.push_back(cnt);
        }
        return answer;
    }
};