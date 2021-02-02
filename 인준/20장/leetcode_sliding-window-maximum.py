'''
Problem Solving leetcode sliding-window-maximum
Author: Injun Son
Date: February 2, 2021
'''
import sys
from collections import deque
from typing import Deque, List

sys.setrecursionlimit(100000)
from collections import deque
import collections
import re


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i: i+ k]))

        return r

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))