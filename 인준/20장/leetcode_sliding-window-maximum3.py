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
    # https://algo.monster/problems/sliding_window_maximum
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # 인덱스들을 저장
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            # 만약 윈도우 밖이면 첫 번째 element를 제거한다
            if q[0] == i - k:
                q.popleft()

            # 맨 처음 인덱스들을 넘어서 윈도우가 만들어지면, 그때부터는 매번 result에 추가한다.
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))