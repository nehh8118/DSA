class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection=[]
        for num in nums1:
            if num in nums2 and num not in intersection: #exists in nums2 and not already in intersection, then add to intersection
                intersection = intersection + [num]
        return intersection


        #req: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.