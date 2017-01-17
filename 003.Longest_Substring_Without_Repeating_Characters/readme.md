  
## 003.Longest_Substring_Without_Repeating_Characters  
  
### **链接**：  
题目：https://leetcode.com/problems/Longest-Substring-Without-Repeating-Characters/  
代码(github)：https://github.com/JianghanLi/LeetCode  
  
### **题意**：  
从标题就可以知道题意了，是求一个字符串中最长的不含重复字符的子串。  
  
### **分析**：  
开一个长度为128(ACSII)或256(拓展ACSII)的数组记录当前字符最近出现的位置。
遍历字符串，根据当前字符出现情况更新左边界，并同时更新长度最大值就行了。  
需要花费常数的空间。
  
  
---  
  
**(English version)**  
  
  
## 003.Longest_Substring_Without_Repeating_Characters  
  
  
**Link**:  
Problem: https://leetcode.com/problems/Longest-Substring-Without-Repeating-Characters/  
Newest solutions in my Github: https://github.com/JianghanLi/LeetCode  
  
**Analysis**：  
Generate an array of size 128(ACSII) or 256(extended ACSII) to record the last position of current character.  
Traverse the string and update the left bound according to occurrence of each char, and calculate the maximum.  
It will just cost constant space.