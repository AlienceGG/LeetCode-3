## 130. Surrounded Regions (Medium)

### **链接**：
题目：https://leetcode.com/problems/surrounded-regions/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个地图，把地图里被 X 包围的 O 块填充为 X。

### **分析**：

1. 找到 O 点就 DFS 填充。不过 DFS 递归是要占用栈的，最糟的空间复杂度是 O(n*n)，这题会卡爆栈，所以 DFS 会 Memory Limit Exceed。  
2. 找到 O 点就 BFS 填充。BFS 才是正解。  

不过一找到 O 就开始处理的话，如果来个全是 O 的，时间复杂度就会变成 O(n*n) 了，就会 TLE，有两种解决方案：1. 开个数组来记录是否访问过，需要 O(n*n) 的空间；2. 遍历 O 的时候把遍历过的 O 而不用变 X 的点变成 +，全部处理后再变回来，这样就不用另开空间了。  

在上面的“把遍历过的 O 而不用变 X 的点变成 +”这个方法中，如果正常去做就要先来一遍 BFS 看看有没有被包围，再一遍 BFS 变点。能不能把两遍 BFS 缩成一遍呢？其实是可以的，我们还是把不用变的化作 '+'，那反过来想，我们只要处理需要化作 '+' 的点不就行了，找到边界的点再 BFS 把 O 变成 +，最后处理时还是 O 的就是可以填充的点了。  
