class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num
        while start<=end:
            mid = (start+end) //2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                end = mid - 1
            else:
                start = mid + 1
        return False

'''
        for i in range(num+1):
            if i*i == num:
                return True
        return False
'''
'''
req: return true if num is a perfect square, else false
approach: using binary search, condition using mid*mid
'''
        