#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
    	map<int, int> container;
    	for(vector<int>::const_iterator ite = nums.begin(); ite!=nums.end(); ite++) {
    		if(container.count(*ite) == 0) {
    			container[*ite] = 1;
    		}else{
    			container[*ite]++;
    		}

    		if(container[*ite] > 1) {
    			return true;
    		}
    	}
    	return false;
    }

    void test() {
    	vector<int> nums(20);
    	for(int i = 0;i<19;i++) {
    		nums[i] = i;
    	}
    	nums[19] = 10;

    	cout<< containsDuplicate(nums) <<endl;
    }
};
