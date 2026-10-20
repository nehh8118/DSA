class Solution:
    def firstNonRepeating(self, arr): 
        # code here
        count={}
        for num in arr:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num in arr:
            if count[num]==1:
                return num
        return 0

n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))

obj = Solution()
result = obj.firstNonRepeating(arr)
print(result)

    #req: return the first non-repeating element in an array, if all elements are repeating return 0
    #approach: The solution uses a dictionary to count the occurrences of each number in the array.
    # It iterates through the array, updating the count for each number.
    # Finally, it checks the counts and returns the first number that appears only once. If all numbers repeat, it returns 0.