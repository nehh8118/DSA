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

n = int(input("Enter the number of elements in the list: "))
nums = list(map(int, input("Enter the elements of the list separated by space: ").split()))

obj = Solution()
result = obj.singleNumber(nums)

print(result)


#req: find the number in the list that appears only once while all other numbers appear twice.
#approach: The solution uses a dictionary to count the occurrences of each number in the list. 
# It iterates through the list, updating the count for each number. 
# Finally, it checks the counts and returns the number that appears only once.