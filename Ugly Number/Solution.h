#include <iostream>

using namespace std;

class Solution {
public:
    
    bool isUgly(int num) {
        if(num == 0) {
            return false;
        }
        int factors[3] = {2, 3, 5};
        for(int i = 0;i<3;i++) {
            while(num%factors[i] == 0) {
                num = num/factors[i];
            }
        }

        return num == 1 ? true : false;
    }

    void test() {
        int n = 40;
        cout<< isUgly(n) <<endl;
    }
};
