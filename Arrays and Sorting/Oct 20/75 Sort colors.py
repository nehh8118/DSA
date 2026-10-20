class Solution:
    def sortColors(self, nums: list[int]) -> None:
        maxVal=max(nums)
        count=[0]*(maxVal+1)

        for num in nums:
            count[num]=count[num]+1

        nums[:]=[]

        for num, freq in enumerate(count):
            nums.extend([num]*freq)

        return nums

solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)

'''
req: Sort an array of integers containing only 0s, 1s, and 2s (representing colors) in-place.
approach: The solution uses a counting sort algorithm to do this
'''

       
        
        