'''
Problem Solving leetcode assign-cookies
Author: Injun Son
Date: February 4, 2021
'''
import heapq
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re
import collections

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count, child_index, cookie_index = 0, 0, 0
        while child_index < len(g) and cookie_index < len(s):
             if g[child_index] > s[cookie_index]:
                cookie_index += 1
                continue
             count += 1
             child_index +=1
             cookie_index += 1
        return count


sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))