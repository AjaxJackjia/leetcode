# 题目

[原链接](https://leetcode.com/problems/ugly-number/)

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include `2`, `3`, `5`. For example, `6`, `8` are ugly while `14` is not ugly since it includes another prime factor `7`.

Note that `1` is typically treated as an ugly number.

# 思路

因为只有被`2,3,5`整除的数才是ugly number，所以直接把用这三个整数去除尽`num`，当最后剩余的`num`不为1时，则此数不为ugly number，否则是ugly number。注意特殊情况，当`num=0`时，直接输出false，否则会报超时。



