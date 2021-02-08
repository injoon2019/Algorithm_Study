'''
Problem Solving leetcode house-robber
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
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[i-2],  dp[i-3])

        return max(dp)

sol = Solution()
print(sol.rob([2,7,9,3,1]))