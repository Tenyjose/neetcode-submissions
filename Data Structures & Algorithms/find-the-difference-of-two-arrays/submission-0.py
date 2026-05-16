class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set,nums2set = set(nums1),set(nums2)
        res1, res2 = [], []

        for num in nums1set:
            if num not in nums2set:
                res1.append(num)

        for num in nums2set:
            if num not in nums1set:
                res2.append(num)

        return [res1,res2]