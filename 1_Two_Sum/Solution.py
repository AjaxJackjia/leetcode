#!/usr/bin/env python
# coding:UTF-8


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
        	for y in range(x, len(nums)):
        		if x != y and (nums[x] + nums[y]) == target:
        			return [x, y]
        return [0, 0]

    def twoSum2(self, nums, target):
		"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 记录已经计算的差值在map中，下次查找时直接看上次结果是否满足条件
		expectMap = dict()
		for index, value in enumerate(nums):
			if value in expectMap:
				return [expectMap[value], index]
			else:
				expectMap[target - value] = index
		return [0, 0]


    def test(self):
    	nums = [2, 7, 11, 15]
    	target = 9
    	print self.twoSum2(nums, target)

    	nums = [3, 2, 4]
    	target = 6
    	print self.twoSum2(nums, target)
