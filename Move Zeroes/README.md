# 题目

[原链接](https://leetcode.com/problems/move-zeroes/)

> Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

> For example, given `nums = [0, 1, 0, 3, 12]`, after calling your function, `nums` should be `[1, 3, 12, 0, 0]`.

**Note:**
 
 * You must do this **in-place** without making a copy of the array.

 * Minimize the total number of operations.

# 思路

根据题目要求，**in-place** 和 最小化操作数，所以我们可以用两个指针：一个指示非零数字的位置，一个指示当前数字的位置，将数组扫一遍之后，就可以将非零数字放到它最终的位置上，然后再将非零数字之后的位置填充`0`就ok了。


