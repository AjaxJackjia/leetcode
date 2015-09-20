#include <iostream>

using namespace std;

class Solution {
public:

    int addDigits(int num) {
        if(num == 0) return 0;
        return num%9 ? num%9 : 9;
    }

    void test() {
        int n = 16;
        cout<< addDigits(n) <<endl;
    }
};
