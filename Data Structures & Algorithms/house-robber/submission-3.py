class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = { }
        n = len(nums)

        def recursive(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i]+recursive(i+2) , recursive(i+1))

            return memo[i]

        return recursive(0)

