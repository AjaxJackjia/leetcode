#!/usr/bin/env python
# coding:UTF-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 2**31 - 1
        # check        
        if x == 0: return 0
        # positive or nagetive
        flag = x > 0 
        x = x if flag else -x

        a = list()
        temp = x
        while temp // 10 != 0:
            a.append(temp % 10)
            temp = temp // 10
        a.append(temp)
        
        # reversed number
        b = 0
        for index, value in enumerate(a):
            b = b + value * 10 ** (len(a) - index - 1) 
        b = b if flag else -b

        # check range
        if flag and b > MAX: return 0
        if (not flag) and b < -MAX: return 0
        return b

    def test(self):
     	print self.reverse(123)
     	print self.reverse(-123)
     	print self.reverse(120)
        print self.reverse(2**32 - 1)
        print self.reverse(-2**32 + 1)
        print self.reverse(0)

