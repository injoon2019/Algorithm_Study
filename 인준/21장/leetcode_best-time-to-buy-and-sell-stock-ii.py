'''
Problem Solving leetcode best-time-to-buy-and-sell-stock-ii
Author: Injun Son
Date: February 3, 2021
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
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 값이 오르는 경우 매번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result