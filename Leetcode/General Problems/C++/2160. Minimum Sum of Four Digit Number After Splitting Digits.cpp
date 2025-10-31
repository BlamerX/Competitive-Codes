class Solution {
public:
    int minimumSum(int num) {
        int arr[4];
        arr[0]=num%10;
        num/=10;
        arr[1]=num%10;
        num/=10;
        arr[2]=num%10;
        num/=10;
        arr[3]=num%10;
        num/=10;
        int num1,num2;
        sort(arr,arr+4);
        num1=(arr[0]*10)+arr[3];
        num2=(arr[1]*10)+arr[2];
        return num1+num2;           
    }
};