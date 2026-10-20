class Solution:
    def largest(self, arr):
        # code here
        max=0
        for i in range(len(arr)): 
            if arr[i]>max: #if the current element is greater than max, update max
                max=arr[i]
        return max

n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))

obj = Solution()
result = obj.largest(arr)
print(result)
                
#req: return the largest element in an array
#approach: The solution initializes a variable `max` to 0 and iterates through the array.
# For each element, it checks if it is greater than the current `max`. If it is, it updates `max` to that element. 
# After checking all elements, it returns the largest value found. 