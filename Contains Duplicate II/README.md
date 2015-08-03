# 题目

[原链接](https://leetcode.com/problems/contains-duplicate-ii/)

> Given an array of integers and an integer `k`, find out whether there there are two distinct indices `i` and `j` in the array such that `nums[i] = nums[j]` and the difference between `i` and `j` is at most `k`.

# 思路

题目需要找到一个数组中的两个数字，这两个数字相等，并且他们的下标之差不超过`k`。

我们可以遍历数组，用`map`来存储数字以及其最近遍历到的数字下标。当碰到一个数字，可以在map中命中，并且其之前的下标与当前下标之差小于`k`时，则返回`true`；否则更新`map`的下标值为当前的下标。（注意，我们所处理的下标默认是按升序排列的）

