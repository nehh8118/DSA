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

n = int(input("Enter the number of elements in the list: "))
nums = list(map(int, input("Enter the elements of the list separated by space: ").split()))

obj = Solution()
result = obj.majorityElement(nums)
print(result)

#req: find the majority element in the list, which is the element that appears more than n/2 times.
#approach: The solution uses a dictionary to count the occurrences of each number in the list.
# If the count of any number exceeds n/2, it returns that number as the majority element.
        
