class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int time=arrivalTime+delayedTime;
        if(time%24==0)
            return 0;
        else
            return time%24;
    }
};