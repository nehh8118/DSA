class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1={}
        for i, num in enumerate(nums):
            dict1[num]=i
        for i, num in enumerate(nums):
            temp=target-nums[i]
            if temp in dict1 and dict1[temp]!=i:
                return [i, dict1[temp]]

        
