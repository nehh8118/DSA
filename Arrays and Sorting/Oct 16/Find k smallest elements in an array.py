class Solution: 
    def FindKSmallest(self, arr, k):
        n = len(arr)     
       
        for i in range(k):  # Run the loop exactly k times
            minIndex = i
            for j in range(i + 1, n):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            
            # Swap elements
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            
        return arr[:k]
    
solution = Solution()
n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))
print("Enter the value of k: ")
k = int(input())
print("The k smallest elements are:", solution.FindKSmallest(arr, k))    

'''
req: Find the k smallest elements in an array.
approach: The solution uses a selection sort algorithm to find the k smallest elements in the array
'''
