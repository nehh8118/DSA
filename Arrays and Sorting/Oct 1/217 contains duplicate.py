class Solution(object):
    def containsDuplicate(self, nums):
        seen = set() #declaring set
        for num in nums:
            if num in seen: #if already in set, then a dup
                return True
            else:
                seen.add(num) #else add it into set
        return False

n = int(input("Enter the number of elements in the list: "))
nums = list(map(int, input("Enter the elements of the list separated by space: ").split()))

obj = Solution()
result = obj.containsDuplicate(nums)
print(result)

#req: check if the list contains any duplicates.
#approach: The solution uses a set to track the numbers seen so far.
# It iterates through the list, checking if each number is already in the set.
# If a number is found in the set, it returns True
        
        
