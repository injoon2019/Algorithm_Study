from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = [1] + [0 for _ in range(len(nums) - 1)]
        right_left = [0 for _ in range(len(nums) - 1)] + [1]
        for i in range(1, len(nums)):
            left_right[i] = nums[i - 1] * left_right[i - 1]
            right_left[-i - 1] = nums[-i] * right_left[-i]
        return [left_right[i] * right_left[i] for i in range(len(nums))]
