class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest=SecondLargest=0
        for num in arr:
            if num>largest: #largest number is found, update largest and second largest
                SecondLargest=largest
                largest=num
            if num>SecondLargest and num<largest: #if the current number is greater than second largest and less than largest, update second largest
                SecondLargest=num
        if SecondLargest==0: #if there is no second largest number in the array, return -1
            return -1
        else:
            return SecondLargest

n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))

obj = Solution()
result = obj.getSecondLargest(arr)
print(result)

#req: return the second largest element in an array
#approach: The solution initializes two variables, `largest` and `SecondLargest`, to 0.
# It iterates through the array, updating `largest` and `SecondLargest` as it
# finds larger numbers. If no second largest number is found, it returns -1.


                
                
                