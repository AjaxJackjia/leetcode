#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    void moveZeroes(vector<int>& nums) {
        int nums_size = nums.size();

        //step 1: move nonzero numbers to left of nums
        int nonzero_pointer = -1;
        int next_nonzero_pointer = 0;
        while(next_nonzero_pointer != nums_size) {
            if(nums[next_nonzero_pointer] != 0) {
                nonzero_pointer++;
                nums[nonzero_pointer] = nums[next_nonzero_pointer];
            }
            next_nonzero_pointer++;
        }

        //step 2: fill nums[nonzero_pointer+1<= x <=nums_size-1] with zero
        for(int i = nonzero_pointer + 1;i<nums_size;i++) {
            nums[i] = 0;
        }
    }

    void display(vector<int>& nums) {
        for(int i = 0;i<nums.size();i++) {
            cout<<nums[i]<<" ";
        }
        cout<<endl;
    }

    void test() {
    	vector<int> nums(5);
        nums[0] = 1;
    	nums[1] = 2;
        nums[2] = 0;
        nums[3] = 3;
        nums[4] = 12;

        moveZeroes(nums);
        display(nums);
    }
};
