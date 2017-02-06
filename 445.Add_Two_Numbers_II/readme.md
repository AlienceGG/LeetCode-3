## 445.Add Two Numbers II (Medium)

### **链接**：
题目：https://leetcode.com/problems/add-two-numbers-ii/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给出两个表示整数的链表，求和

### **分析**：
1. 转化为整数相加在思路上可行，但是有的test case的值会导致long long溢出，造成结果错误
2. 存入array或stack再处理，改变取值方向