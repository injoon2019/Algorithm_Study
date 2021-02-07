'''
Problem Solving leetcode different-ways-to-add-parentheses
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
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1: ])

                results.extend(compute(left, right, value))

        return results

sol = Solution()
print(sol.diffWaysToCompute("2-1-1"))