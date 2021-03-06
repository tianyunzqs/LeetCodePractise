# -*- coding: utf-8 -*-
# @Time        : 2020/7/9 10:09
# @Author      : tianyunzqs
# @Description : 

"""
198. House Robber
Easy

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    def rob0(self, nums: list) -> int:
        pre_max_amount, cur_max_amount = 0, 0
        for num in nums:
            tmp = max(pre_max_amount + num, cur_max_amount)
            pre_max_amount = cur_max_amount
            cur_max_amount = tmp
        return cur_max_amount

    def rob(self, nums: list) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # dp[i]表示抢到第i个house时，已抢到的最大金额
        dp = [0] * len(nums)
        # 只有一个house
        dp[0] = nums[0]
        # 只有两个house，选最大的
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 不能抢相邻house
            # dp[i-2] + nums[i]表示往前推2个house的最大金额加上当前house
            # dp[i-1]表示与往前推1个house的最大金额
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]


if __name__ == '__main__':
    # print(Solution().rob([2, 7, 9, 3, 1]))
    print(Solution().rob([2, 1, 7, 2, 3, 9, 3, 1]))
