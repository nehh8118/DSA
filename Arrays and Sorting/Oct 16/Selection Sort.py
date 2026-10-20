class Solution: 
    def selectionSort(self, arr):
        # code here
        n=len(arr)
        for i in range(n): #to run for n times in an arr
            minIndex=i #assigning to the first element
            for j in range(i+1, n): #assumin elements till i are sorteed
                if arr[j] < arr[minIndex]: 
                    minIndex=j #update minindex as lower element found
            arr[i], arr[minIndex] = arr[minIndex], arr[i] #swap with found

        return arr

solution = Solution()
n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))
print("The sorted array is:", solution.selectionSort(arr))

''' 
req: Sort an array of integers using selection sort algorithm.
approach: The solution uses a selection sort algorithm to sort the array. It iterates through the array, finds the minimum element
 in the unsorted portion, and swaps it with the first unsorted element. 
 This process is repeated until the entire array is sorted.
 '''