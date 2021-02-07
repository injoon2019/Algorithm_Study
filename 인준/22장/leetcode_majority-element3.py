'''
Problem Solving leetcode majority-element
Author: Injun Son
Date: February 7, 2021
'''
import heapq
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re
import collections
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))