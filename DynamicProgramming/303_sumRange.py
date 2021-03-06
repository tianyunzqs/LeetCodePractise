# -*- coding: utf-8 -*-
# @Time        : 2020/8/21 20:59
# @Author      : tianyunzqs
# @Description ：

"""
303. Range Sum Query - Immutable
Easy

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Constraints:
You may assume that the array does not change.
There are many calls to sumRange function.
0 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= i <= j < nums.length
"""

from typing import List


class NumArray0:
    """
    元素之和
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums:
            return 0
        return sum(self.nums[i:j+1])


class NumArray:
    """
    在init函数中计算累计和，主要是为了提升实时计算时的速度
    跟更动态规划的思想相吻合
    """
    def __init__(self, nums: List[int]):
        self.accu = [0]
        for num in nums:
            self.accu.append(self.accu[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.accu[j+1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 3))
