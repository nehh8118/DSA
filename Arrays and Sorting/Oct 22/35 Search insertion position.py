def searchInsert(nums, target):
    left=0
    right=len(nums) - 1
        
    while left <= right:
        mid = (right + left) // 2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
                
    return left

sorted=[2, 4, 7, 8, 45, 77, 90]
print("Position in array:", searchInsert(sorted, 98))

'''
req: to find pos of the given element in array, if not found, give pos if it was inserted int the sorted array
approach: using binary search to find pos, if not found, returning thr starting value of the sub array
'''