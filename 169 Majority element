class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        n=len(nums)
        for num in nums:   #dictionary with num and thier counts
            if num in count:
                count[num]=count[num]+1
            else:
                count[num]=1
        for key in count:  #is count greater than specified
            if count[key]>n/2:
                return key
        
        
