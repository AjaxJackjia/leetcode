# 题目

[原链接](https://leetcode.com/problems/ugly-number-ii/)

Write a program to find the `n`-th ugly number.

Ugly numbers are positive numbers whose prime factors only include `2, 3, 5`. For example, `1, 2, 3, 4, 5, 6, 8, 9, 10, 12` is the sequence of the first `10` ugly numbers.

Note that `1` is typically treated as an ugly number.

# 思路

最naive的方法就是利用ugly number中的方法，对每个自然数进行判断，直到找到第n个ugly number，这种方法超时；

我们可以看到每次生成的ugly number都是前一个ugly number乘以`2, 3, 5`中的最小数，所以我们只要有三个队列，分别保存乘以`2, 3, 5`生成的ugly number，然后每次取其中队列头部最小的一个数作为下一个ugly number，重复n次这个过程，就可以得到第n个ugly number。

