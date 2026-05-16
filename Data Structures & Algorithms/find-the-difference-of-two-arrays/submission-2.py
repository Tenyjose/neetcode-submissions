class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set,nums2set = set(nums1),set(nums2)


        return [list(nums1set - nums2set) , list(nums2set - nums1set)]