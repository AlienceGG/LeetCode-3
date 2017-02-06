## 445.Add Two Numbers II (Medium)

### **链接**：
题目：https://leetcode.com/problems/add-two-numbers-ii/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给出两个表示整数的链表，求和

### **分析**：
1. 转化为整数相加在思路上可行，但是有的test case的值会导致long long溢出，造成结果错误
2. 存入array或string或stack再处理，改变取值方向， 空间复杂度为O(n)
3. 先得两链表长度，正序取值相加，再建立新链表反向存储各位数未进位的和，并正序读取此链表处理进位，优势是空间复杂度降为O(1)
4. 迭代法