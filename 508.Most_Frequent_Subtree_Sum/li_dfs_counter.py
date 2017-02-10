# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-04 11:51-12:06


# Definition for a binary tree node.
class TreeNode(object):

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

from collections import Counter


class Solution(object):

  def findFrequentTreeSum(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # import collections
    # ctr = collections.Counter()
    ctr = Counter()
    if root == None:
      return []
    self.countSubtreeSum(root, ctr)
    return [i for i in ctr.keys() if ctr[i] == max(ctr.values())]

  def countSubtreeSum(self, root, ctr):
    if root == None:
      return 0
    else:
      val = self.countSubtreeSum(root.left, ctr) + \
          self.countSubtreeSum(root.right, ctr) + root.val
      ctr[val] += 1
      return val


s = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
print s.findFrequentTreeSum(root)


# I have used a hash-map ctr to count the sum occurrence.

# I have wrote a sub function countSubtreeSum to travel through a tree and
# return the sum of the tree.

# In countSubtreeSum, I will travel through the left node and the right node,
# calculate the sum of the tree, increment the counter ctr, and return the sum.

# https://discuss.leetcode.com/topic/77769/python-easy-understand-solution
