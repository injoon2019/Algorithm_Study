'''
Problem Solving leetcode fibonacci-number
Author: Injun Son
Date: February 8, 2021
'''
import sys
from collections import deque
from typing import Deque, List

sys.setrecursionlimit(100000)
from collections import deque
import collections
import re


class Solution:
    def fib(self, n: int) -> int:
        ans = [0] * 31
        ans[0] = 0
        ans[1] = 1
        for i in range(2, 31):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]

sol = Solution()
print(sol.fib(3))