def BinarySearch(arr, target):
    low=0
    high=len(arr)-1

    while low<high:
        mid=(low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]> target:
            high=mid-1
        else:
            low=mid+1
    return -1

sorted=[2, 4, 7, 8, 45, 77, 90]
print("Position in array:", BinarySearch(sorted, 8))

'''
req: To search an element in an array usign binary search
approach: To set a mid value and compare if the element to be foun is lower or higher that mid value, 
if it is lower, search in left sub array, otherwise right subarray
'''

