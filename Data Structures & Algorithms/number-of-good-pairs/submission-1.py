class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        count = defaultdict(int)

        for num in nums:
            pairs += count[num]
            count[num] += 1
           

        return pairs
