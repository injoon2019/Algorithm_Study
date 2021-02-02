'''
Problem Solving leetcode minimum-window-substring
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
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1): # 1부터 시작하겠다는 의미다.
            missing -= need[char] > 0 # 만약 현재 문자가 필요한 문자 need[char]에 포함되어 있다면
            # 필요한 문자의 전체 개수인 missing을 1 감소한다.
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right

                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))