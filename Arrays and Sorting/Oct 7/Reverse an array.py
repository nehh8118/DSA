def reverseArray(arr):
    l=0
    r=len(arr)-1
    while l<r:
        arr[l], arr[r]=arr[r], arr[l]
        l+=1
        r-=1
    return arr

print(reverseArray([1, 2, 3, 4, 5, 6, 7]))

'''
req: Reverse an array
approach: Use two pointers, one starting from the beginning and the other from the end of
 the array. Swap the elements at these pointers and move them towards each other until they meet in the middle.
'''