class Solution
{
public:
    // In statistics, the median is used for dividing a set into two equal length subsets
	// that one subset is always greater than the other
	// the key is to use binary search to divide sets here
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
		int m = nums1.size(), n = nums2.size();
		
		// let nums1 shorter than nums2
		if (m > n)
			return findMedianSortedArrays(nums2, nums1);
		
		// init
		int i, j, imin = 0, imax = m, half_len = (m + n + 1) / 2;
		
		
		while (imin <= imax)
		{
			i = (imin + imax) / 2;
			j = half_len - i;
			
			if (i < m && nums2[j-1] > nums1[i])
			{
				// i is too small, must increase it
				imin = i + 1;
			}
			else if (i > 0 && nums1[i-1] > nums2[j])
			{
				// i is too big, must decrease it
				imax = i - 1;
			}
			else
			{
				// i is perfect
				break;
			}
		}
		
		// Get max of left subset
		int max_of_left;
		if (i == 0)
			max_of_left = nums2[j-1];
		else if (j == 0)
			max_of_left = nums1[i - 1];
		else
			max_of_left = max(nums1[i-1], nums2[j-1]);
		
		// Odd number case
		 if ((m + n) % 2 != 0)
			 return max_of_left;
		
		// Even number case
		// Get min of right subset
		int min_of_right;
		if (i == m) 
			min_of_right = nums2[j];
        else if (j == n) 
			min_of_right = nums1[i];
        else 
			min_of_right = min(nums1[i], nums2[j]);
		
        return (max_of_left + min_of_right) / 2.0;
    }
};