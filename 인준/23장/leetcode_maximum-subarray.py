'''
Problem Solving leetcode maximum-subarray
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
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return max(dp)

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))