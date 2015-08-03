# 题目

[原链接](https://leetcode.com/problems/contains-duplicate/)

> Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# 思路

利用map来存储已经遍历的值的个数，一旦达到要求就`return true`，否则`return false`.
