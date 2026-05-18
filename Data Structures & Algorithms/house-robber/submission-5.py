class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2  = 0
        prev1 = 0

        for money in nums:
            current_money = max(prev2+money,prev1)

            prev2 = prev1   # best money upto previuos house
            prev1 = current_money

        return prev1
