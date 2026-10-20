class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1={}
        for i, num in enumerate(nums):
            dict1[num]=i
        for i, num in enumerate(nums):
            temp=target-nums[i]
            if temp in dict1 and dict1[temp]!=i:
                return [i, dict1[temp]]
        return []
    
n = int(input("Enter the number of elements in the list: "))
nums = list(map(int, input("Enter the elements of the list separated by space: ").split()))
target = int(input("Enter the target value: "))

obj = Solution()
result = obj.twoSum(nums, target)

print(result)

#req: find two numbers in the list that add up to the target and return their indices. 
# Approach: The solution uses a dictionary to store the numbers and their indices for quick lookup.
#  It iterates through the list, calculates the complement of each number with respect to the target, 
# and checks if that complement exists in the dictionary. If it does and is not the same index, it returns the indices of the two numbers.  
        
