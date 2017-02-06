# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-06 10:25

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
    v1, v2 = 0, 0
    while l1:
      v1 *= 10
      v1 += l1.val
      l1 = l1.next


s = Solution()
print s.nextGreaterElements([1, 2, 1])
