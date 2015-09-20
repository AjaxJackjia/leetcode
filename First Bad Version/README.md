# 题目

[原链接](https://leetcode.com/problems/first-bad-version/)

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which will return whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# 思路

如果发现一个版本是bad的，那么它后面的版本必然是bad的，所以只要找到左边界就ok。因为题目要限制调用函数的次数，所以使用二分查找，如果当前版本是bad的，那么左边界存在于它的左半边，否则左边界存在于它的右边。注意，在获取中间位置的时候，应该使用`mid = start + (end - start)/2`防止溢出。


