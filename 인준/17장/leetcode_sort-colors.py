'''
Problem Solving leetcode largest-number
Author: Injun Son
Date: January 29, 2021
'''
import sys
import collections
import heapq
import functools
import itertools
import re
import math
import bisect
from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()