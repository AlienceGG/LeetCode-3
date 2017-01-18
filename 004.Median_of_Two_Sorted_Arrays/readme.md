
## 004.Median_of_Two_Sorted_Arrays

### **链接**：
题目：https://leetcode.com/problems/Median-of-Two-Sorted-Arrays/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
求两个有序数组的中位数。要求复杂度是 O(log(n + m))。

### **分析**：
两种思路：  
1. 直接 merge 两个数组，然后求中位数，能过，不过复杂度是 O(n + m)。  
2. 从中位数的计算公式出发，分奇偶情况，转化思维，去求两个有序数组中的第 K 大数 (二分法)，再计算中位数。  
3. 从中位数的定义出发，将两个数组再分为长度相等的两组，一组数全部小于另一组。
若总个数为奇，中位数就是小组最大数，若为偶，则为小组最大数和大组最小数的平均值。

---

**(English version)*

## 004.Median_of_Two_Sorted_Arrays


**Link**:
Problem: https://leetcode.com/problems/Median-of-Two-Sorted-Arrays/  
Newest solutions in my Github: https://github.com/JianghanLi/LeetCode

**Analysis**：
Two ways to get it.  
1. Merge the two arrays first and solve it. But the time complexity is O(n + m).  
2. From formula of median, calculate it on 2 cases : odd or even number of elements.
The problem can then be seen as to find the k-th biggest number in two sorted arrays (by binary search).  
3. From the definition of median in statistics, we can divide the 2 arrays to form 2 subsets of equal length that one subset is always greater than the other
So if there are odd number of elements, the median will be max of smaller set, else, it will be (max of smaller set + min of greater set )/ 2