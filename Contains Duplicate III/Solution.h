#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {

    }

    void test() {
    	int k = 3, t = 2;
    	vector<int> nums(20);
    	for(int i = 0;i<19;i++) {
    		nums[i] = i;
    	}
    	nums[19] = 10;

    	cout<< containsNearbyAlmostDuplicate(nums, k, t) <<endl;
    }
};
