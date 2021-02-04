'''
Problem Solving leetcode task-scheduler
Author: Injun Son
Date: February 4, 2021
'''
import heapq
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아티메을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result

sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))