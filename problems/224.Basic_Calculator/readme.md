## 224. Basic Calculator (Medium)

### **链接**：
题目：https://leetcode.com/problems/basic-calculator/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

实现一个只有 `+-()` 的计算器。

### **分析**：

题目已经说不能用 `eval` 这种内建函数了。  
由于只有 `+-`，题目难度小了很多。

1. 主要的难点在括号，在遇到括号时可以把之前算好的结果和括号前的符号放到栈里，括号结束后再取出来计算。
2. 用小学时学的去括号来做，括号前面是 `-` 要变号，这也要一个栈来保存每个 ( 前的符号。
3. 当然可以用递归来做，遇到左括号时进递归，右括号退出。
