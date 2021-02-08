'''
Problem Solving leetcode climbing-stairs
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
    def climbStairs(self, n: int) -> int:
        dp = [0] * 50
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, 46):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

