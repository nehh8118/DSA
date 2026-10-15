class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[0]*n
        res[0] = nums[0]
        for i in range(1,n):
            res[i] = res[i-1] + nums[i]
        return res


            
#req: Given an array nums, return an array runningSum where runningSum[i] is the sum of all elements from index 0 to i in nums.