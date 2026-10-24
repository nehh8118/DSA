def FloorCeil(nums, target):
    n=len(nums)
    start, end = 0, n-1
    floor, ceil = -1, -1

    while start<=end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return (target, target)
        elif nums[mid] < target: #smaller than target
            floor = nums[mid]
            start = mid+1 #look for a larger floor at right
        else:
            ceil = nums[mid]
            end = mid-1 #look for a smaller ceil at left

    return [floor, ceil]

print(FloorCeil([1, 2, 8, 10, 11, 12, 19], 5))

'''
req: find floor and ceil in a given sorted array, 
    floor: largest num that is smaller than x
    ceil: smallest num that is greater than x
approach: binary search
'''