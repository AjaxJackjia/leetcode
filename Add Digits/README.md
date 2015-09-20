# 题目

[原链接](https://leetcode.com/problems/add-digits/)

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given `num = 38`, the process is like: `3 + 8 = 11, 1 + 1 = 2.` Since `2` has only one digit, return it.

**Follow up:**

Could you do it without any loop/recursion in O(1) runtime?


# 思路

这个题目要求用O(1)的时间复杂度来实现，也就是说可以跟剧`num`的值直接得到结果。我们可以很容易知道，最终的返回结果只有10中可能，然后再来猜测到底这几种结果的出现有无规律。

0 => 0

1 => 1 	 10 => 1 	 19 => 1

2 => 1 	 11 => 2 	 20 => 2

3 => 3 	 12 => 3 	 21 => 3

4 => 4 	 13 => 4 	 22 => 4

5 => 5 	 14 => 5 	 23 => 5

6 => 6 	 15 => 6 	 24 => 6

7 => 7 	 16 => 7 	 25 => 7

8 => 8 	 17 => 8 	 26 => 8

9 => 9 	 18 => 9 	 27 => 9 	 ...

从上面可以很容易看到规律，0是比较特殊的，其余的数字可以由 `num%9 ? num%9 : 9`推导出来。
