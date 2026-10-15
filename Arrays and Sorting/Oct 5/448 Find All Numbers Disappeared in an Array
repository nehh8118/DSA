class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=[]
        hashset=set(nums)
        for i in range(1, len(nums)+1):
            if i not in hashset:
                res+=[i]
        return res
        

        #req: Given an array nums of n integers where nums[i] is in the range [1, n], 
        # return an array of all the integers in the range [1, n] that do not appear in nums.