class Solution:
    def reverseInGroups(self, arr, k):
        """code here"""
        n=len(arr)
        for i in range(0, n, k):
            start=i
            end=min(i+k-1, n-1)
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1
        return arr

solution = Solution()
print(solution.reverseInGroups([1, 2, 3, 4, 5, 6, 7], 3))

''' 
req: Rotate an array in groups as per the given value of k
approach: Divide the array into groups of k elements and reverse each group individually.
    create a loop with step count of n, using min func to find the smallest end and reverse as per requirement
'''
                
        
