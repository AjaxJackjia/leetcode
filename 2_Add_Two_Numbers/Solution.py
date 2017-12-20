#!/usr/bin/env python
# coding:UTF-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cursor1 = l1
        cursor2 = l2
        tenFlag = 0
        while True:
            cursor1Val = cursor1.val if cursor1 is not None else 0
            cursor2Val = cursor2.val if cursor2 is not None else 0
            sumTmp = cursor1Val + cursor2Val + tenFlag
            tenFlag = 1 if sumTmp >= 10 else 0
            if cursor1 == l1 and cursor2 == l2:
                sumList = ListNode(sumTmp%10)
                cursorSum = sumList
            else:
                cursorSum.next = ListNode(sumTmp%10)
                cursorSum = cursorSum.next
        
            if cursor1 is not None: 
                cursor1 = cursor1.next
            if cursor2 is not None: 
                cursor2 = cursor2.next
            
            if (cursor1 is None) and (cursor2 is None):
                break
        if tenFlag:
            cursorSum.next = ListNode(1)
        return sumList

    def display(self, l):
        cursor = l
        print cursor.val, 
        while cursor.next is not None:
            print " -> ", cursor.next.val, 
            cursor = cursor.next
        print ""

    def test(self):
        a1 = ListNode(2)
        a2 = ListNode(4)
        a3 = ListNode(3)
        l1 = a1
        a1.next = a2
        a2.next = a3

        b1 = ListNode(5)
        b2 = ListNode(6)
        b3 = ListNode(4)
        l2 = b1
        b1.next = b2
        b2.next = b3

        self.display(l1)
        self.display(l2)
        l3 = self.addTwoNumbers(l1, l2)
        self.display(l3)
        

        l1 = ListNode(5)
        l2 = ListNode(5)
        self.display(l1)
        self.display(l2)
        l3 = self.addTwoNumbers(l1, l2)
        self.display(l3)




