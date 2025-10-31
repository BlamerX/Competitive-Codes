class ParkingSystem {
public:
int big,medium,small;
    ParkingSystem(int big1, int medium1, int small1) {
        big=big1;
        medium=medium1;
        small=small1;
    }
    
    bool addCar(int carType) {
        // 1 for big
        // 2 for medium
        // 3 for small
        if(carType==1){
            if(big==0)
                return false;
            big--;
        }else if(carType==2){
            if(medium==0)
                return false;
            medium--;   
        }else{
            if(small==0)
                return false;
            small--;
        }
        return true;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */