#include <iostream>
#include <deque>

using namespace std;

class Solution {
public:

    int nthUglyNumber(int n) {
        int min = 0;

        deque<int> queue1;
        deque<int> queue2;
        deque<int> queue3;

        queue1.push_back(1);
        queue2.push_back(1);
        queue3.push_back(1);

        for(int i = 0;i<n;i++) {
            //find min
            min = queue1.front();
            if(min > queue2.front()) {
                min = queue2.front();
            }
            if(min > queue3.front()) {
                min = queue3.front();
            }

            //pop min
            if(min == queue1.front()) queue1.pop_front();
            if(min == queue2.front()) queue2.pop_front();
            if(min == queue3.front()) queue3.pop_front();

            //add new element
            queue1.push_back(min * 2);
            queue2.push_back(min * 3);
            queue3.push_back(min * 5);
        }

        return min;
    }

    void test() {
        int n = 16;
        cout<< nthUglyNumber(n) <<endl;
    }
};
