#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
    	map<int, unsigned int> container;
    	for(unsigned int index = 0;index!=nums.size(); index++) {
    		int current = nums[index];
    		if(container.count(current) == 0) {
    			container[current] = index;
    		}else if(index - container[current] <= k) {
    			return true;
    		}else{
    			container[current] = index;
    		}
    	}
    	return false;
    }

    void test() {
    	int k = 3;
    	vector<int> nums(20);
    	for(int i = 0;i<19;i++) {
    		nums[i] = i;
    	}
    	nums[19] = 10;

    	cout<< containsNearbyDuplicate(nums, k) <<endl;
    }
};
