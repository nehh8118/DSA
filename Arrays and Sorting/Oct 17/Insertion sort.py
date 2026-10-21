def InsertionSort(arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key
    return arr

arr= [34, 34, 56, 31, 6]
print(InsertionSort(arr))

'''
req: Sort an array using insertion sort algorithm
approach: The insertion sort algorithm sorts an array by repeatedly taking an element from the unsorted portion 
and inserting it into the correct position in the sorted portion. It works by comparing the current element with 
the elements in the sorted portion and shifting them to make space for the current element.
'''