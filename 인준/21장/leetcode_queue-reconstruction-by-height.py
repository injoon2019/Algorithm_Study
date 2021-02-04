'''
Problem Solving leetcode queue-reconstruction-by-height
Author: Injun Son
Date: February 4, 2021
'''
import heapq
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], (-person[0], person[1]))
        return result

sol = Solution()
print(sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))