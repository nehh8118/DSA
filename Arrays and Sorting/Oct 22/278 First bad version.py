# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (r + l) // 2
            if isBadVersion(mid):
                r = mid  #left half, including mid
            else:
                l = mid + 1  #right half
        return l


