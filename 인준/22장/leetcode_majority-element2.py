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
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b,a][nums.count(a) > half] # a가 만약 현재 분할된 리스트 nums에서 과반수를 차지한다면 해당 인덱스는 1이 될 것이고,
                                            # [b,a][1]이 되어 a를 리턴할 것이다. 즉 과반수인 엘리먼트를 리턴한다. 이외에는 b를 리턴한다.

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))