# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-30 21:45


class Solution(object):
  from queue import PriorityQueue as PQueue

  def findShortestWay(self, maze, ball, hole):
    """
    :type maze: List[List[int]]
    :type ball: List[int]
    :type hole: List[int]
    :rtype: str
    """

    m, n = len(maze), len(maze[0])
    x0, y0 = ball
    x1, y1 = hole
    # ret
    ret = [['' for i in range(n)] for j in range(m)]
    # ret[x0][y0] = "S"
    # bfs initialisation
    bfsList = PQueue()
    (x, y) = (x0, y0)
    maze[x0][y0] = 1
    while (x, y) != (x1, y1):
      if x > 0 and maze[x - 1][y] == 0:
        bfsList.append((x - 1, y))
        maze[x - 1][y] = 1
        ret[x - 1][y] = ret[x][y] + 'u'
      if x < m - 1 and maze[x + 1][y] == 0:
        bfsList.append((x + 1, y))
        maze[x + 1][y] = 1
        ret[x + 1][y] = ret[x][y] + 'd'
        print ret, x, y
      if y > 0 and maze[x][y - 1] == 0:
        bfsList.append((x, y - 1))
        maze[x][y - 1] = 1
        ret[x][y - 1] = ret[x][y] + 'l'
      if y < n - 1 and maze[x][y + 1] == 0:
        bfsList.append((x, y + 1))
        maze[x][y + 1] = 1
        ret[x][y + 1] = ret[x][y] + 'r'
      if len(bfsList):
        (x, y) = bfsList.pop()
      else:
        break
      for l in maze:
        print l
      for l in ret:
        print l
    return ret[x1][y1]

s = Solution()
print s.findShortestWay([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],
                        [4, 3],
                        [0, 1])
