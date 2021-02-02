'''
Problem Solving leetcode number-of-1-bits
Author: Injun Son
Date: February 1, 2021
'''
import sys
from collections import deque
from typing import Deque, List

sys.setrecursionlimit(100000)
from collections import deque
import collections
import re


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n ^ 0).count('1')