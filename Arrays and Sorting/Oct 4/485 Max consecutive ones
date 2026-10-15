class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxcount=0
        count=0
        for num in nums:
            if num==1:
                count+=1
            if count>maxcount: #updating maxcount if count is greater than maxcount
                maxcount=count    
            if num==0: #resetting count to 0 if we encounter a 0 in the array
                count=0

        return maxcount
        