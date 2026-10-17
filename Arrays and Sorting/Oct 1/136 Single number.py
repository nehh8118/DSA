class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count={}
        for i, num in enumerate(nums): #accessing both index and element in the array
            if num in count:
                count[num]+=1 #increment count if already exists
            else:
                count[num]=1
        for num in count: #return if count is 1
            if count[num]==1:
                return num
        