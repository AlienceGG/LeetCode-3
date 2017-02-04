class Solution(object):

  def majorityElement(self, nums):
    import collections
    ctr = collections.Counter()
    for n in nums:
      ctr[n] += 1
      if len(ctr) == 3:
        ctr -= collections.Counter(set(ctr))
    return [n for n in ctr if nums.count(n) > len(nums) / 3]


s = Solution()
print s.majorityElement([])
print s.majorityElement([3, 2, 3])
print s.majorityElement([1, 2, 1, 2, 5])

#
