class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def reverse(start: int, end: int) -> None:
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        n=len(nums)
        k=k%n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        return nums

solution = Solution()
print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))

'''
req: Rotate an array by k steps to the right
approach: reverse the whole array, reverse the first k elements, then reverse the n-k elements
'''



                

        
        